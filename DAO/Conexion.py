import pymysql
from contextlib import contextmanager

class Conexion:
    def __init__(self, host="localhost", user="root", password="", bdd="ECHOTECH_SOLUTIONS", port=3306):
        # Agrupamos todos los parámetros en un diccionario de configuración
        self.config = {
            "host": host,
            "user": user,
            "password": password,
            "database": bdd,      
            "port": port,
            "autocommit": False  
        }
        
    @contextmanager
    def conectar(self):
        try:
            conexion = pymysql.connect(**self.__config)

            yield conexion
        
        except Exception:
            self.rollback(conexion)

        finally:
            self.desconectar(conexion)



