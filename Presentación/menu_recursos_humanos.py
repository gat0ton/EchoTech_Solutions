import getpass
from DTO.Persona.empleado_dto import EmpleadoDTO
from DTO.Administracion.departamento_dto import DepartamentoDTO
from Presentación.menu_area import MenuArea

class MenuRecursosHumanos(MenuArea):

    # Cada opción indica en el comentario qué clase del diagrama la ejecuta.
    _OPCIONES = [
        # --- Administrador ---
        ("Registrar usuario", "registrar_usuario"),
        ("Registrar empleado", "registrar_empleado"),
        ("Modificar salario", "modificar_salario"),                          # GestorRecursosHumanos.modificarSalario()
        ("Crear departamento", "crear_departamento"),
        ("Editar departamento", "editar_departamento"),
        ("Buscar departamento", "buscar_departamento"),                      # GestorRecursosHumanos.buscarDepartamento()
        ("Eliminar departamento", "eliminar_departamento"),                  # GestorRecursosHumanos.eliminarDepartamento()
        ("Asignar empleado a departamento", "asignar_departamento"),         # GestorRecursosHumanos.asignarEmpleadoADepartamento()
        ("Asignar gerente a departamento", "asignar_gerente"),               # GestorRecursosHumanos.asignarGerente()
        ("Informe de empleados", "generar_informes"),                      # GeneradorInformes.exportarInformeEmpleados()
        ("Informe de departamentos", "generar_informes"),                    # GeneradorInformes.exportarInformeDepartamentos()
        # --- Empleado ---
        ("Ver mi perfil", "ver_perfil"),                                     # Empleado.obtenerPerfilPublico()
        ("Ver mis datos de contacto", "ver_contacto"),                       # Persona.obtenerContacto()
        ("Ver mi ficha completa", "ver_ficha"),                              # Empleado.obtenerFichaCompleta()
        ("Modificar mis datos", "modificar_mis_datos"),
    ]

    # Implementación obligatoria de los métodos abstractos de MenuArea.
    def obtenerTitulo(self):
        return "RECURSOS HUMANOS"

    def obtenerOpciones(self):
        return self._OPCIONES

    def ejecutar(self, accion):
        if accion == "registrar_usuario":
            self._registrarUsuario()
        elif accion == "registrar_empleado":
            self._registrarEmpleado()
        elif accion == "crear_departamento":
            self._crearDepartamento()
        elif accion == "editar_departamento":
            self._editarDepartamento()
        elif accion == "modificar_mis_datos":
            self._modificarMisDatos()
        else:
            super().ejecutar(accion)

    def _registrarEmpleado(self):
        print("\n--- REGISTRAR EMPLEADO ---")
        try:
            username = input("Nombre de usuario: ").strip()
            id_empleado = int(input("ID de empleado: ").strip())
            nombre = input("Nombre: ").strip()
            apellido = input("Apellido: ").strip()
            edad = int(input("Edad: ").strip())
            genero = input("Genero: ").strip()
            telefono = input("Telefono (+56 ): ").strip()
            direccion = input("Direccion: ").strip()
            correo = input("Correo: ").strip()
            salario = float(input("Salario: ").strip())
            puesto = input("Puesto: ").strip()
            departamento = input("Departamento: ").strip()
            if not departamento:
                raise ValueError("El empleado debe estar asociado a un departamento.")
            clave = getpass.getpass("Contraseña inicial: ")
            confirmacion = getpass.getpass("Repita la contraseña: ")
            empleado = EmpleadoDTO(
                id_empleado, nombre, apellido, edad, genero, telefono, direccion,
                correo, 0, salario, puesto, username, departamento
            )
            self.servicio.registrarEmpleado(
                self.usuario, empleado, clave, confirmacion
            )
            print(f"Empleado '{username}' registrado correctamente.")
        except (ValueError, PermissionError, RuntimeError) as error:
            print(f"Error: {error}")

    def _crearDepartamento(self):
        print("\n--- CREAR DEPARTAMENTO ---")
        try:
            nombre = input("Nombre: ").strip()
            descripcion = input("Descripción: ").strip()
            responsable_id = int(input("ID del administrador o gerente responsable: "))
            self.servicio.registrarDepartamento(
                self.usuario,
                DepartamentoDTO(nombre, descripcion, responsable_id),
            )
            print("Departamento registrado correctamente.")
        except (ValueError, PermissionError, RuntimeError) as error:
            print(f"Error: {error}")

    def _editarDepartamento(self):
        print("\n--- EDITAR DEPARTAMENTO ---")
        try:
            nombre = input("Nombre del departamento: ").strip()
            descripcion = input("Nueva descripción: ").strip()
            responsable_id = int(input("Nuevo ID del administrador o gerente responsable: "))
            self.servicio.actualizarDepartamento(
                self.usuario, nombre, descripcion, responsable_id
            )
            print("Departamento actualizado correctamente.")
        except (ValueError, PermissionError, RuntimeError) as error:
            print(f"Error: {error}")

    def _modificarMisDatos(self):
        print("\n--- MODIFICAR MIS DATOS ---")
        try:
            nuevo_username = input("Nuevo nombre de usuario: ").strip()
            telefono = input("Nuevo teléfono: ").strip()
            direccion = input("Nueva dirección: ").strip()
            correo = input("Nuevo correo: ").strip()
            self.servicio.actualizarMiEmpleado(
                self.usuario, nuevo_username, telefono, direccion, correo
            )
            print("Datos actualizados correctamente.")
        except (ValueError, PermissionError, RuntimeError) as error:
            print(f"Error: {error}")

    def _registrarUsuario(self):
        # Por ahora crea solo la cuenta de acceso. Al implementar Empleado, esta opción debe pasar a GestorRecursosHumanos.registrarEmpleado(), que crea la ficha del empleado y su cuenta juntas.
        
        print("\n--- REGISTRAR USUARIO ---")

        username = input("Nombre de usuario: ").strip()
        print("Rol: 1. Empleado  2. Administrador")
        rol = {"1": "Empleado", "2": "Administrador"}.get(input("Seleccione el rol: ").strip())
        if rol is None:
            print("Rol no válido.")
            return

        clave = getpass.getpass("Contraseña inicial (mínimo 8 caracteres, con letras y números): ")
        confirmacion = getpass.getpass("Repita la contraseña: ")

        # Presentación → Negocio: se envía el usuario de la sesión para que el servicio verifique el permiso.
        try:
            self.servicio.registrarUsuario(self.usuario, username, clave, confirmacion, rol)
            print(f"Usuario '{username}' registrado correctamente como {rol}.")
        # ErrorPersistencia hereda de RuntimeError.
        except (ValueError, PermissionError, RuntimeError) as error:
            print(f"Error: {error}")