from abc import ABC, abstractmethod

class MenuArea(ABC):

    def __init__(self, usuario, servicio_autenticacion):
        self.usuario = usuario
        self.servicio = servicio_autenticacion

    @abstractmethod
    def obtener_titulo(self):
        """Título del área que se muestra en el menú principal y en el encabezado."""

    @abstractmethod
    def obtener_opciones(self):
        """Lista de opciones del área: (texto que se muestra, acción que debe estar permitida)."""

    def opciones_disponibles(self):
        return [(texto, accion) for texto, accion in self.obtener_opciones()
                if self.usuario.verificar_autorizacion(accion)]

    def tiene_opciones(self):
        return len(self.opciones_disponibles()) > 0

    def mostrar_menu(self):
        while True:
            opciones = self.opciones_disponibles()
            volver = len(opciones) + 1

            print("\n" + "*" * 44)
            print(self.obtener_titulo().center(44))
            print(f"Usuario: {self.usuario.obtener_identidad()}".center(44))
            print("*" * 44 + "\n")
            for numero, (texto, _) in enumerate(opciones, 1):
                print(f"{numero:>4}. {texto}")
            print(f"{volver:>4}. Volver al menú principal\n")

            try:
                opcion = int(input("Seleccione una opción: "))
            except ValueError:
                print("Opción inválida: ingrese un número.")
                continue

            if opcion == volver:
                return
            if not 1 <= opcion <= len(opciones):
                print(f"Opción no válida. Elija un número del 1 al {volver}.")
                continue

            self.ejecutar(opciones[opcion - 1][1])

    def ejecutar(self, accion):
        print("Funcionalidad pendiente de implementar.")
