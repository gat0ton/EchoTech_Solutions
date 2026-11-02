from persona import Persona as p

class Administrador(p):
    def __init__(
                    self, 
                    id: int, nombre: str, apellido: str, edad: int, genero: str, telefono: str, direccion: str, correo: str, horas: int, inicioContrato: str, salario: float, presupuesto: float):
            
        super().__init__(id, nombre, apellido, edad, genero, telefono, direccion, correo, horas, inicioContrato, salario)
        self.__presupuesto = presupuesto

    class DatosAdministrador(p.AbcDatos):
        presupuesto: float

    def __str__(self):
        return f"""
        Persona: {self._nombre} {self._apellido}, 
        ID: {self._id},
        Edad: {self._edad},
        Género: {self._genero},
        Teléfono: {self._telefono},
        Dirección: {self._direccion},
        Correo: {self._correo},
        Horas: {self._horas}, 
        Salario: {self._salario},
        Inicio Contrato: {self._inicioContrato}
        Presupuesto Asignado: {self.__presupuesto}
        {'='* 40}"""

    
    
    def _actualizar_datos(self, datos: dict[str, object]):
        for campo, valor in datos.items():
            if hasattr(self, campo):
                setattr(self, campo, valor)
                return True
            else:
                return False


