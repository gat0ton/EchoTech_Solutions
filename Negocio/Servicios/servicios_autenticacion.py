from Negocio.Servicios.verificador_password import VerificadorPassword
from DTO.usuario_dto import UsuarioDTO
from Negocio.usuario import Usuario

ROL_ADMINISTRADOR = "Administrador"
LARGO_MINIMO_CLAVE = 8

# Negocio: recibe las peticiones de la presentación, aplica las reglas y usa el DAO para leer o guardar.
class ServicioAutenticacion:

    def __init__(self, usuario_dao):
        if usuario_dao is None:
            raise ValueError("ServicioAutenticacion necesita un DAO de usuarios.")
        self.usuario_dao = usuario_dao
        self._verificador = VerificadorPassword()

    def autenticarUsuario(self, username, clave):
        if not username or not clave:
            return None

        # 1. Negocio → Persistencia: el DAO busca el usuario y lo devuelve como DTO.
        dto = self.usuario_dao.buscarPorUsername(username)
        if dto is None:
            return None

        # 2. DTO → dominio: se crea el objeto Usuario con los datos guardados.
        usuario = Usuario(dto.username, dto.passwordHash, dto.rol)

        # 3. El servicio calcula el hash de la clave ingresada con la misma salt del hash guardado;el dominio lo compara y activa la sesión.
        if usuario.autenticar(username, self._verificador.generarComoGuardado(clave, dto.passwordHash)):
            return usuario
        return None

    def registrarUsuario(self, usuario_sesion, username, clave, confirmacion, rol):
        # La presentación ya oculta la opción a quien no tiene permiso, pero la regla de seguridad real está aquí: ninguna capa puede registrar usuarios sin una sesión autorizada.
        if usuario_sesion is None or not usuario_sesion.verificarAutorizacion("registrar_usuario"):
            raise PermissionError("No tiene autorización para registrar usuarios.")

        self._registrar(username, clave, confirmacion, rol)

    def existeAdministrador(self):
        # Permite a Main saber si hace falta la configuración inicial.
        return self.usuario_dao.existeRol(ROL_ADMINISTRADOR)

    def registrarPrimerAdministrador(self, username, clave, confirmacion):
        # Única operación sin sesión: crea el administrador inicial durante la instalación.Solo se permite mientras no exista ninguno; después, los usuarios se registran desde el sistema.
        if self.existeAdministrador():
            raise PermissionError("Ya existe un administrador. Los nuevos usuarios se registran desde el sistema.")

        self._registrar(username, clave, confirmacion, ROL_ADMINISTRADOR)

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
        # 1. Validar los datos de entrada.
        if not username or not clave:
            raise ValueError("El usuario y la contraseña son obligatorios.")
        if len(username) > 50:
            raise ValueError("El nombre de usuario no puede superar los 50 caracteres.")
        self._validarClave(clave, confirmacion)

        # 2. Crear el objeto de dominio; la contraseña se transforma en hash antes de entregársela.
        passwordHash = self._verificador.generar(clave)
        usuario = Usuario(username, passwordHash, rol)

        # 3. El dominio aplica su regla; el servicio informa si la rechazó.
        if not usuario.tieneRolValido():
            raise ValueError("El rol no es válido.")
        if self.usuario_dao.buscarPorUsername(username) is not None:
            raise ValueError("El nombre de usuario ya existe.")

        # 4. Dominio → DTO → Persistencia: el DAO recibe un DTO y lo guarda en la BD.
        self.usuario_dao.agregar(UsuarioDTO(None, usuario.obtenerIdentidad(), passwordHash, usuario.obtenerRol()))