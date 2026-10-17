from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(self,
        __id: int,
        __nombre: str,
        __apellido: str,
        __edad: int,
        __telefono: str,
        __direccion: str,
        __correo: str
    ):
        self.__id = __id
        self.__nombre = __nombre
        self.__apellido = __apellido
        self.__edad = __edad
        self.__telefono = __telefono
        self.__direccion = __direccion        
        self.__correo = __correo

    @abstractmethod
    def _consultar_datos(self):
        pass

    @abstractmethod
    def _actualizar_datos(self, params):
        pass

