from os import error

from .Menu.logica import Logica
from DAO.conexion import Conexion

class Flujo:

    @staticmethod
    def ejecutar():
        Logica.principal()

