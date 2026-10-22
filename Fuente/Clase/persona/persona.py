from abc import ABC, abstractmethod
from typing import TypedDict


class Persona(ABC):
    class AbcDatos(TypedDict, total=False):
        id: int
        nombre: str
        apellido: str
        edad: int
        genero: str
        telefono: str
        direccion: str
        correo: str
        horas: int
        salario: float

    @abstractmethod
    def __init__(
            self,
        id: int,
        nombre: str,
        apellido: str,
        edad: int,
        genero: str,
        telefono: str,
        direccion: str,
        correo: str,
        horas: int,
        salario: float):
        
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._genero = genero
        self._telefono = telefono
        self._direccion = direccion
        self._correo = correo
        self._horas = horas
        self._salario = salario

        
        

    @abstractmethod
    def _consultar_datos(self):
        pass

    
    @abstractmethod
    def _actualizar_datos(self, datos: frozendict) -> str:
        pass

