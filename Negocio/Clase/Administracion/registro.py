from typing import TypedDict
from abc import abstractmethod

class Registro:
    class DatosRegistro(TypedDict):
        horas: int
        fecha: str

    def __init__(self,
                 horas: int,
                 fecha: str,
                 id_asociado: int):
        self.__horas = horas
        self.__fecha = fecha
        self.__id_asociado = id_asociado

    
    def __str__(self):
        return f"""
        {'='* 40}
        Horas: {self.__horas}
        Fecha: {self.__fecha}
        ID Asociado: {self.__id_asociado}
        {'='* 40}
        """

    @property
    def horas(self):
        return self.__horas

    @property
    def fecha(self):
        return self.__fecha

    @property
    def id_asociado(self):
        return self.__id_asociado
        
        
        