from Presentación.menu_recursos_humanos import MenuRecursosHumanos
from Presentación.menu_proyectos import MenuProyectos
import getpass


class MenuPrincipal:

    def __init__(self, usuario, servicio_autenticacion):
        self.usuario = usuario
        self.servicio = servicio_autenticacion

    def mostrarMenu(self):
        areas = [
            menu for menu in (
                MenuRecursosHumanos(self.usuario, self.servicio),
                MenuProyectos(self.usuario, self.servicio),
            )
            if menu.tieneOpciones()
        ]

        if not areas:
            print("\nEl usuario no tiene un rol reconocido.")
            self.usuario.cerrarSesion()
            return

        cambiar = len(areas) + 1
        cerrar = len(areas) + 2

        while True:
            print("\n" + "*" * 44)
            print("MENÚ PRINCIPAL".center(44))
            print(f"Usuario: {self.usuario.obtenerIdentidad()} ({self.usuario.obtenerRol()})".center(44))
            print("*" * 44 + "\n")
            for numero, menu in enumerate(areas, 1):
                print(f"{numero:>4}. {menu.obtenerTitulo().capitalize()}")
            print(f"{cambiar:>4}. Cambiar contraseña")
            print(f"{cerrar:>4}. Cerrar sesión\n")

            try:
                opcion = int(input("Seleccione una opción: "))
            except ValueError:
                print("Opción inválida: ingrese un número.")
                continue

            if 1 <= opcion <= len(areas):
                areas[opcion - 1].mostrarMenu()
            elif opcion == cambiar:
                self._cambiarPassword()
            elif opcion == cerrar:
                self.usuario.cerrarSesion()
                print("Sesión finalizada.")
                return
            else:
                print(f"Opción no válida. Elija un número del 1 al {cerrar}.")

    def _cambiarPassword(self):
        print("\n--- CAMBIAR CONTRASEÑA ---")
        claveActual = getpass.getpass("Contraseña actual: ")
        claveNueva = getpass.getpass("Contraseña nueva (mínimo 8 caracteres, con letras y números): ")
        confirmacion = getpass.getpass("Repita la contraseña nueva: ")

        try:
            self.servicio.cambiarPassword(self.usuario, claveActual, claveNueva, confirmacion)
            print("Contraseña actualizada correctamente.")
        except (ValueError, RuntimeError) as error:
            print(f"Error: {error}")