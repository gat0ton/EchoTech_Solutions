from Negocio.Servicios.verificador_password import VerificadorPassword
from DTO.usuario_dto import UsuarioDTO
from DTO.Administracion.proyecto_dto import ProyectoDTO
from Negocio.Clase.Administracion.proyecto import Proyecto
from Negocio.Clase.Administracion.registro import Registro
from Negocio.Servicios.api_moneda import API
from Negocio.usuario import Usuario

ROL_ADMINISTRADOR = "Administrador"
LARGO_MINIMO_CLAVE = 8

# Negocio: recibe las peticiones de la presentación, aplica las reglas y usa el DAO para leer o guardar.
class ServicioAutenticacion:

    def __init__(
        self, usuario_dao, empleado_dao=None, departamento_dao=None, proyecto_dao=None
    ):
        if usuario_dao is None:
            raise ValueError("ServicioAutenticacion necesita un DAO de usuarios.")
        self.usuario_dao = usuario_dao
        self.empleado_dao = empleado_dao
        self.departamento_dao = departamento_dao
        self.proyecto_dao = proyecto_dao
        self._verificador = VerificadorPassword()
        self._api_moneda = API()

    _MONEDAS_POR_PAIS = {
        "argentina": "ARS",
        "brasil": "BRL",
        "canada": "CAD",
        "chile": "CLP",
        "colombia": "COP",
        "españa": "EUR",
        "espana": "EUR",
        "estados unidos": "USD",
        "méxico": "MXN",
        "mexico": "MXN",
        "perú": "PEN",
        "peru": "PEN",
        "uruguay": "UYU",
    }

    def autenticarUsuario(self, username, clave):
        if not username or not clave:
            return None

        # Negocio → Persistencia: el DAO busca el usuario y lo devuelve como DTO.
        dto = self.usuario_dao.buscarPorUsername(username)
        if dto is None:
            return None

        #  DTO → dominio: se crea el objeto Usuario con los datos guardados.
        usuario = Usuario(dto.username, dto.passwordHash, dto.rol)

        #  El servicio calcula el hash de la clave ingresada con la misma salt del hash guardado;el dominio lo compara y activa la sesión.
        if usuario.autenticar(username, self._verificador.generarComoGuardado(clave, dto.passwordHash)):
            return usuario
        return None

    def registrarUsuario(self, usuario_sesion, username, clave, confirmacion, rol):
        # La presentación ya oculta la opción a quien no tiene permiso, pero la regla de seguridad real está aquí: ninguna capa puede registrar usuarios sin una sesión autorizada.
        if usuario_sesion is None or not usuario_sesion.verificarAutorizacion("registrar_usuario"):
            raise PermissionError("No tiene autorización para registrar usuarios.")

        self._registrar(username, clave, confirmacion, rol)

    def registrarEmpleado(self, usuario_sesion, empleado_dto, clave, confirmacion):
        if usuario_sesion is None or not usuario_sesion.verificarAutorizacion("registrar_empleado"):
            raise PermissionError("No tiene autorización para registrar empleados.")
        if self.empleado_dao is None:
            raise ValueError("No hay un DAO de empleados configurado.")
        if not empleado_dto.username:
            raise ValueError("El nombre de usuario es obligatorio.")
        self._validarClave(clave, confirmacion)
        rol = "Administrador" if empleado_dto.puesto.lower().startswith(
            ("administrador", "gerente")
        ) else "Empleado"
        self._registrar(empleado_dto.username, clave, confirmacion, rol)
        self.empleado_dao.agregar(empleado_dto)

    def actualizarMiEmpleado(self, usuario_sesion, nuevo_username, telefono, direccion, correo):
        if self.empleado_dao is None:
            raise ValueError("No hay un DAO de empleados configurado.")
        empleado = self.empleado_dao.buscarPorUsername(usuario_sesion.obtenerIdentidad())
        if empleado is None:
            raise ValueError("No existe una ficha asociada al usuario.")
        if not nuevo_username:
            raise ValueError("El nombre de usuario es obligatorio.")
        username_anterior = usuario_sesion.obtenerIdentidad()
        self.empleado_dao.actualizarContacto(
            username_anterior, nuevo_username, telefono, direccion, correo
        )
        self.usuario_dao.actualizarUsername(username_anterior, nuevo_username)
        usuario_sesion.actualizarIdentidad(nuevo_username)

    def registrarDepartamento(self, usuario_sesion, departamento):
        self._validarGestionDepartamentos(usuario_sesion, departamento.responsable_id)
        if self.departamento_dao is None:
            raise ValueError("No hay un DAO de departamentos configurado.")
        self.departamento_dao.agregar(departamento)

    def actualizarDepartamento(self, usuario_sesion, nombre, descripcion, responsable_id):
        self._validarGestionDepartamentos(usuario_sesion, responsable_id)
        if self.departamento_dao is None:
            raise ValueError("No hay un DAO de departamentos configurado.")
        self.departamento_dao.actualizar(nombre, descripcion, responsable_id)

    def registrarProyecto(self, usuario_sesion, proyecto_dto: ProyectoDTO):
        if usuario_sesion is None or not usuario_sesion.verificarAutorizacion(
            "crear_proyecto"
        ):
            raise PermissionError("No tiene autorización para registrar proyectos.")
        if self.proyecto_dao is None:
            raise ValueError("No hay un DAO de proyectos configurado.")

        pais = proyecto_dto.pais.strip()
        moneda = self._MONEDAS_POR_PAIS.get(pais.casefold())
        if moneda is None:
            raise ValueError("No hay una moneda configurada para ese país.")

        conversion = self._api_moneda.convertir_clp(proyecto_dto.presupuesto_clp, moneda)
        registro = Registro(
            proyecto_dto.registro_horas,
            proyecto_dto.registro_fecha,
            proyecto_dto.registro_id_asociado,
        )
        proyecto = Proyecto(
            proyecto_dto.nombre,
            proyecto_dto.departamento_nombre,
            registro,
            pais,
            conversion["monto_clp"],
            conversion["moneda_destino"],
            conversion["monto_convertido"],
            conversion["tasa"],
        )
        return self.proyecto_dao.agregar(
            ProyectoDTO(
                proyecto.nombre,
                proyecto.departamento,
                proyecto.registro.horas,
                proyecto.registro.fecha,
                proyecto.registro.id_asociado,
                proyecto.pais,
                proyecto.presupuesto_clp,
                proyecto.moneda,
                proyecto.presupuesto_local,
                proyecto.tasa_conversion,
            )
        )

    def consultarProyecto(self, usuario_sesion, proyecto_id):
        self._validarConsultaProyecto(usuario_sesion)
        proyecto = self.proyecto_dao.buscarDetalle(proyecto_id)
        if proyecto is None:
            raise ValueError("No existe un proyecto con ese ID.")
        return proyecto

    def consultarHistorialProyecto(self, usuario_sesion, proyecto_id):
        self._validarConsultaProyecto(usuario_sesion)
        if self.proyecto_dao.buscarDetalle(proyecto_id) is None:
            raise ValueError("No existe un proyecto con ese ID.")
        return self.proyecto_dao.historialRegistros(proyecto_id)

    def asociarEmpleadoProyecto(self, usuario_sesion, proyecto_id, empleado_id):
        if usuario_sesion is None or not usuario_sesion.verificarAutorizacion(
            "asignar_proyecto"
        ):
            raise PermissionError("No tiene autorización para asociar empleados.")
        if self.proyecto_dao is None:
            raise ValueError("No hay un DAO de proyectos configurado.")
        self.proyecto_dao.asociarEmpleado(proyecto_id, empleado_id)

    def _validarConsultaProyecto(self, usuario_sesion):
        if usuario_sesion is None or not usuario_sesion.verificarAutorizacion(
            "consultar_proyecto"
        ):
            raise PermissionError("No tiene autorización para consultar proyectos.")
        if self.proyecto_dao is None:
            raise ValueError("No hay un DAO de proyectos configurado.")

    def _validarGestionDepartamentos(self, usuario_sesion, responsable_id):
        if usuario_sesion is None:
            raise PermissionError("Se necesita una sesión para modificar departamentos.")
        if self.empleado_dao is None:
            raise ValueError("No hay un DAO de empleados configurado.")
        empleado_actual = self.empleado_dao.buscarPorUsername(
            usuario_sesion.obtenerIdentidad()
        )
        if (
            empleado_actual is None
            or not empleado_actual.puesto.lower().startswith(("administrador", "gerente"))
        ):
            raise PermissionError(
                "Solo un administrador o gerente puede modificar departamentos."
            )
        responsable = self.empleado_dao.buscarPorId(responsable_id)
        if responsable is None or not responsable[1].lower().startswith(
            ("administrador", "gerente")
        ):
            raise ValueError(
                "El responsable debe tener puesto de Administrador o Gerente."
            )

    def existeAdministrador(self):
        # Permite a Main saber si hace falta la configuración inicial.
        return self.usuario_dao.existeRol(ROL_ADMINISTRADOR)

    def registrarPrimerAdministrador(self, username, clave, confirmacion, empleado_dto=None):
        # Única operación sin sesión: crea el administrador inicial durante la instalación.Solo se permite mientras no exista ninguno; después, los usuarios se registran desde el sistema.
        if self.existeAdministrador():
            raise PermissionError("Ya existe un administrador. Los nuevos usuarios se registran desde el sistema.")

        if empleado_dto is not None and self.empleado_dao is None:
            raise ValueError("No hay un DAO de empleados configurado.")

        self._registrar(username, clave, confirmacion, ROL_ADMINISTRADOR)
        if empleado_dto is not None:
            self.empleado_dao.agregar(empleado_dto)

    def cambiarPassword(self, usuario, claveActual, claveNueva, confirmacion):
        self._validarClave(claveNueva, confirmacion)

        # El servicio calcula los hashes: la clave actual con la salt del hash guardado, y la nueva con una salt nueva. El dominio verifica la clave actual y la sesión.
        dto = self.usuario_dao.buscarPorUsername(usuario.obtenerIdentidad())
        if dto is None:
            raise ValueError("La cuenta de usuario ya no existe.")
        hashActual = self._verificador.generarComoGuardado(claveActual, dto.passwordHash)
        hashNuevo = self._verificador.generar(claveNueva)
        if not usuario.cambiarPassword(hashActual, hashNuevo):
            raise ValueError("La contraseña actual no es correcta.")

        # Negocio → Persistencia: se guarda el nuevo hash.
        self.usuario_dao.actualizarPassword(usuario.obtenerIdentidad(), hashNuevo)
        return True

    def validarClave(self, clave, confirmacion):
        self._validarClave(clave, confirmacion)

    def _validarClave(self, clave, confirmacion):
        # La contraseña se escribe dos veces para evitar errores de tipeo.
        if clave != confirmacion:
            raise ValueError("Las contraseñas no coinciden.")

        # Política de contraseña segura: largo mínimo y combinación de letras y números.
        if len(clave) < LARGO_MINIMO_CLAVE:
            raise ValueError(f"La contraseña debe tener al menos {LARGO_MINIMO_CLAVE} caracteres.")
        if not any(caracter.isalpha() for caracter in clave):
            raise ValueError("La contraseña debe contener al menos una letra.")
        if not any(caracter.isdigit() for caracter in clave):
            raise ValueError("La contraseña debe contener al menos un número.")

    def _registrar(self, username, clave, confirmacion, rol):
        # Validar los datos de entrada.
        if not username or not clave:
            raise ValueError("El usuario y la contraseña son obligatorios.")
        if len(username) > 50:
            raise ValueError("El nombre de usuario no puede superar los 50 caracteres.")
        self._validarClave(clave, confirmacion)

        # Crear el objeto de dominio; la contraseña se transforma en hash antes de entregársela.
        passwordHash = self._verificador.generar(clave)
        usuario = Usuario(username, passwordHash, rol)

        # El dominio aplica su regla; el servicio informa si la rechazó.
        if not usuario.tieneRolValido():
            raise ValueError("El rol no es válido.")
        if self.usuario_dao.buscarPorUsername(username) is not None:
            raise ValueError("El nombre de usuario ya existe.")

        # Dominio → DTO → Persistencia: el DAO recibe un DTO y lo guarda en la BD.
        self.usuario_dao.agregar(UsuarioDTO(None, usuario.obtenerIdentidad(), passwordHash, usuario.obtenerRol()))