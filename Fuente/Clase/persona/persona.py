from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(self,
        id: int,
        nombre: str,
        apellido: str,
        edad: int,
        genero: str,
        telefono: str,
        direccion: str,
        correo: str):
        
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__genero = genero
        self.__telefono = telefono
        self.__direccion = direccion        
        self.__correo = correo

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def edad(self):
        return self.__edad

    @property
    def genero(self):
        return self.__genero

    @property
    def telefono(self):
        return self.__telefono

    @property
    def direccion(self):
        return self.__direccion

    @property
    def correo(self):
        return self.__correo


    @abstractmethod
    def _consultar_datos(self):
        pass

    @classmethod
    @abstractmethod
    def _actualizar_datos(cls, datos: dict[str, object]):
        return NotImplementedError("Este método debe ser implementado en la subclase.")
