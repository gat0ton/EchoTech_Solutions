from .persona import Persona as p

class Administrador(p):
    def __init__(
                    self, 
                    __id: int, _nombre: str, _apellido: str, _edad: int, _genero: str, _telefono: str, _direccion: str, _correo: str, _horas: int, _salario: float,
                    departamento: Departamento):
            
        super().__init__(__id, _nombre, _apellido, _edad, _genero, _telefono, _direccion, _correo, _horas, _salario)

        self.__departamento = departamento

    class DatosAdministrador(p.AbcDatos):
        departamento: Departamento
    
    def __str__(self):
        return f"""{'='* 40}
        Administrador: {self._nombre} {self._apellido}, 
        ID: {self._id},
        Edad: {self._edad},
        Género: {self._genero},
        Teléfono: {self._telefono},
        Dirección: {self._direccion},
        Correo: {self._correo},
        Departamento: {self.__departamento}, 
        Horas: {self._horas}, 
        Salario: {self._salario}
        {'='* 40}"""

    
    
    def _actualizar_datos(self, datos: dict[str, object]):
        for campo, valor in datos.items():
            if hasattr(self, campo):
                setattr(self, campo, valor)