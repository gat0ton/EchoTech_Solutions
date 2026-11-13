from os import error

from .Menu.logica import Logica
from Fuente.Persistencia.conexion import Conexion

class Flujo:

    @staticmethod
    def ejecutar():
        Logica.principal()

