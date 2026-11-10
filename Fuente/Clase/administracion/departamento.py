from Persona.administrador import Administrador
from Persona.empleado import Empleado


class Departamento:
    def __init__(self,
                 nombre : str,
                 gerente: Administrador,
                 empleados: list[Empleado],
                 horas: int):
        
        self.__nombre = nombre
        self.__gerente = gerente
        self.__empleados = empleados
        self.__horas = horas

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def __str__(self):
        return f"""
        {'-'* 40}
        Departamento: {self.__nombre}
        Gerente: {self.__gerente._nombre} {self.__gerente._apellido}
        Empleados: {[empleado._nombre + ' ' + empleado._apellido for empleado in self.__empleados]}
        Horas: {self.__horas}
        {'-'* 40}"""

    