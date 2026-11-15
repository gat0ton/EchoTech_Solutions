from .persona import Persona as p
from Clase.Administracion.registro import Registro


class Empleado(p):
    def __init__(
                self, _id: int, _nombre: str, _apellido: str, _edad: int, _genero: str, _telefono: str, _direccion: str, _correo: str, _horas: int, _salario: float,
                    puesto: str
                 ):
        
        super().__init__(_id, _nombre, _apellido, _edad, _genero, _telefono, _direccion, _correo, _horas, _salario)
        
        self.__puesto = puesto
    class DatosEmpleado(p.AbcDatos):
        puesto: str

    
    
    def __str__(self):
        return f"""
        {'='* 40}
        Empleado: {self._nombre} {self._apellido}
        ID: {self._id}
        Edad: {self._edad}
        Género: {self._genero}
        Teléfono: {self._telefono}
        Dirección: {self._direccion}
        Correo: {self._correo}
        Puesto: {self.__puesto}
        Horas: {self._horas}
        Salario: {self._salario}"""
    

    
    

    

    def _actualizar_datos(self, datos: frozendict[str, object]):
        for campo, valor in datos.items():
            if hasattr(self, campo):
                setattr(self, campo, valor)
                return True
            else:
                return False
    