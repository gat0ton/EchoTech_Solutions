from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(
        self,
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
    def __consultar_datos(self):
        return self.__id, self.__nombre, self.__apellido, self.__edad, self.__telefono, self.__direccion, self.__correo

    @abstractmethod
    def __actualizar_datos(
                        self,
                             input_id: int, 
                             input_nombre: str, input_apellido: str, 
                             input_edad: int, input_telefono: str, 
                             input_direccion: str, input_puesto: str, input_horas: int, 
                             input_salario: float
                             
                             ):
        pass    



