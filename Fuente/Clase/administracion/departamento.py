from Fuente.Clase.persona.empleado import Empleado


class Departamento:
    def __init__(self,
                 nombre : str,
                 gerente: Empleado,
                 empleados: list[Empleado]):
        
        self.nombre = nombre
        self.gerente = gerente
        self.empleados = empleados

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    