from abc import ABC, abstractmethod

class MenuArea(ABC):

    def __init__(self, usuario, servicio_autenticacion):
        self.usuario = usuario
        self.servicio = servicio_autenticacion

    @abstractmethod
    def obtenerTitulo(self):
        """Título del área que se muestra en el menú principal y en el encabezado."""

    @abstractmethod
    def obtenerOpciones(self):
        """Lista de opciones del área: (texto que se muestra, acción que debe estar permitida)."""

    def opcionesDisponibles(self):
        return [(texto, accion) for texto, accion in self.obtenerOpciones()
                if self.usuario.verificarAutorizacion(accion)]

    def tieneOpciones(self):
        return len(self.opcionesDisponibles()) > 0

    def mostrarMenu(self):
        while True:
            opciones = self.opcionesDisponibles()
            volver = len(opciones) + 1

            print("\n" + "*" * 44)
            print(self.obtenerTitulo().center(44))
            print(f"Usuario: {self.usuario.obtenerIdentidad()}".center(44))
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
