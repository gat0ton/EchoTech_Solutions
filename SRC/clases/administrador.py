from persona import Persona
from empleado import Empleado

import inspect


class Administrador(Persona):
    def __init__(self, 
                 numeroPersona: int,
                    nombre: str, 
                    apellido: str, 
                    telefono: str, 
                    correo: str, 
                    direccion: str, 
                    contraseña: str,
                    area: str):
        
        
        super().__init__(
                    numeroPersona,
                    nombre,
                    apellido,
                    telefono,
                    correo,
                    direccion,
                    contraseña
                )
        
        self._area = area
        self._empleados = [] # Lista temporal.

    def consultarDatos(self):
        return (
            f"Número: {self._numeroPersona}\n"
            f"Nombre: {self._nombre} {self._apellido}\n"
            f"Teléfono: {self._telefono}\n"
            f"Correo: {self._correo}\n"
            f"Dirección: {self._direccion}\n"
            f"Área: {self._area}"
        )

    def iniciarSesion(self, correo, contraseña):
        if self._correo == correo and self._contraseña == contraseña:
            return True
        return False

    def cambiarContraseña(self, nuevaContraseña):
        self._contraseña = nuevaContraseña
        return True

    def registrarEmpleado(self, empleado: Empleado):
        self._empleados.append(empleado)
        return f"Empleado {empleado._nombre} {empleado._apellido} registrado exitosamente."

    def buscarEmpleado(self, numeroPersona: int):
        for empleado in self._empleados:
            if empleado._numeroPersona == numeroPersona:
                return f"Empleado encontrado: {empleado._nombre} {empleado._apellido}"
        return f"Empleado con el ID {numeroPersona} no encontrado."

