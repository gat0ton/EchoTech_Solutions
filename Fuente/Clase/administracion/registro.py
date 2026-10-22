from typing import TypedDict
from abc import abstractmethod

class Registro:    
    def __init__(self,
                 horas: int,
                 fecha: str,
                 entrada: bool):
        self.__horas = horas
        self.__fecha = fecha
        self.__entrada = entrada

    
    def __str__(self):
        return f"""
        {'='* 40}
        Horas: {self.__horas}
        Fecha: {self.__fecha}
        Entrada: {self.__entrada}
        """
        
        
        