import getpass
from Presentación.menu_area import MenuArea

class MenuRecursosHumanos(MenuArea):

    # Cada opción indica en el comentario qué clase del diagrama la ejecuta.
    _OPCIONES = [
        # --- Administrador ---
        ("Registrar usuario", "registrar_usuario"),                          # Implementado (ServicioAutenticacion)
        ("Registrar empleado", "registrar_empleado"),                        # GestorRecursosHumanos.registrarEmpleado()
        ("Modificar salario", "modificar_salario"),                          # GestorRecursosHumanos.modificarSalario()
        ("Crear departamento", "crear_departamento"),                        # GestorRecursosHumanos.crearDepartamento()
        ("Editar departamento", "editar_departamento"),                      # GestorRecursosHumanos.editarDepartamento()
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
    ]

    # Implementación obligatoria de los métodos abstractos de MenuArea.
    def obtenerTitulo(self):
        return "RECURSOS HUMANOS"

    def obtenerOpciones(self):
        return self._OPCIONES

    def ejecutar(self, accion):
        if accion == "registrar_usuario":
            self._registrarUsuario()
        else:
            super().ejecutar(accion)

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