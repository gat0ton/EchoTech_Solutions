import getpass
import time
from DTO.Persona.empleado_dto import EmpleadoDTO


class Login:

    _INTENTOS = 3

    def __init__(self, servicio_autenticacion):
        if servicio_autenticacion is None:
            raise ValueError("Login necesita un servicio de autenticación")
        self.servicio = servicio_autenticacion

    def iniciarSesion(self):
        for restantes in range(self._INTENTOS - 1, -1, -1):
            print("\n" + "*" * 36)
            print("ECOTECH SOLUTIONS".center(36))
            print("INICIO DE SESIÓN".center(36))
            print("*" * 36)

            try:
                username = input("Nombre de usuario: ").strip()
                clave = getpass.getpass("Contraseña: ")
            except (EOFError, KeyboardInterrupt):
                print("\nInicio de sesión cancelado.")
                return None

            if not username or not clave:
                print("\nUsuario y contraseña no pueden estar vacíos.")
                continue

            try:
                usuario = self.servicio.autenticarUsuario(username, clave)
            except RuntimeError:
                return None

            if usuario is not None:
                return usuario

            
            print("\nUsuario o contraseña incorrectos.")
            print("Por favor, espere un momento antes de reintentar...")
            time.sleep(2)

            if restantes:
                print(f"Intentos restantes: {restantes}.")

        print("\nSe alcanzó el máximo de intentos. Acceso denegado.")
        return None

    def crearPrimerAdministrador(self):
        print("\n" + "=" * 44)
        print("ECOTECH SOLUTIONS".center(44))
        print("CONFIGURACIÓN INICIAL".center(44))
        print("=" * 44)
        print("El sistema no tiene administradores.")
        print("Cree el usuario administrador para comenzar.\n")

        try:
            username = input("Nombre de usuario: ").strip()
            id_empleado = input("ID de empleado: ").strip()
            nombre = input("Nombre: ").strip()
            apellido = input("Apellido: ").strip()
            edad = input("Edad: ").strip()
            genero = input("Genero: ").strip()
            telefono = input("Telefono (+56 ): ").strip()
            direccion = input("Direccion: ").strip()
            correo = input("Correo: ").strip()
            salario = input("Salario: ").strip()
            puesto = input("Puesto: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nConfiguración cancelada.")
            return False

        while True:
            try:
                clave = getpass.getpass("Contraseña (mínimo 8 caracteres, con letras y números): ")
                confirmacion = getpass.getpass("Repita la contraseña: ")
                self.servicio.validarClave(clave, confirmacion)
                break
            except ValueError as error:
                print(f"\n{error}\nIntente nuevamente la contraseña.")
            except (EOFError, KeyboardInterrupt):
                print("\nConfiguración cancelada.")
                return False

        try:
            empleado = EmpleadoDTO(
                int(id_empleado),
                nombre,
                apellido,
                int(edad),
                genero,
                telefono,
                direccion,
                correo,
                0,
                float(salario),
                puesto,
            )
            self.servicio.registrarPrimerAdministrador(
                username,
                clave,
                confirmacion,
                empleado,
            )
        except (ValueError, PermissionError) as error:
            print(f"\n{error}")
            return False
        
        except RuntimeError:
            print("\nError al acceder a la base de datos.")
            return False

        print(f"\nAdministrador '{username}' creado correctamente. Ya puede iniciar sesión.")
        return True