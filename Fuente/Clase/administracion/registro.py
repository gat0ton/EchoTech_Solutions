from typing import TypedDict
from abc import abstractmethod

class Registro:
    class DatosRegistro(TypedDict):
        horas: int
        fecha: str

    def __init__(self,
                 horas: int,
                 fecha: str):
        self.__horas = horas
        self.__fecha = fecha

    
    def __str__(self):
        return f"""
        {'='* 40}
        Horas: {self.__horas}
        Fecha: {self.__fecha}
        """
        
        
        