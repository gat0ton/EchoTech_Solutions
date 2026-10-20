from .persona import Persona as p

class administrador(p):
    def __init__(
                self, __id: int, __nombre: str, __apellido: str, __edad: int, __genero: str, __telefono: str, __direccion: str,
                    __correo: str,
                    puesto: str,
                    horas: int,
                    salario: float,
                    administrador: bool = True
                 
                 ):
        
        super().__init__(__id, __nombre, __apellido, __edad, __genero, __telefono, __direccion, __correo)
        
        self.__puesto = puesto
        self.__horas = horas
        self.__salario = salario
        self.__administrador = administrador

    
    def __str__(self):
        return f"""
        {'='* 40}
        Administrador: {self.__nombre} {self.__apellido}, 
        ID: {self.__id},
        Edad: {self.__edad},
        Género: {self.__genero},
        Teléfono: {self.__telefono},
        Dirección: {self.__direccion},
        Correo: {self.__correo},
        Puesto: {self.__puesto}, 
        Horas: {self.__horas}, 
        Salario: {self.__salario}"""

    
    
    @classmethod
    def _actualizar_datos(cls, datos: dict[str, object]):
        for campo, valor in datos.items():
            if hasattr(cls, campo):
                setattr(cls, campo, valor)