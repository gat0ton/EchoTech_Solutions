import pymysql
from contextlib import contextmanager

class Conexion:
    def __init__(self, host="localhost", user="root", password="", bdd="ECHOTECH_SOLUTIONS", port=3306):
        # Agrupamos todos los parámetros en un diccionario de configuración
        self.__config = {
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
            print("Conexion Exitosa")

            yield conexion
        
        except Exception:
            self.rollback(conexion)
            print(":((((")

        finally:
            self.desconectar(conexion)

    def rollback(self, conexion):
        conexion.rollback()

    def desconectar(self, conexion):
        conexion.close()

conexion = Conexion()

def ahora():
    with conexion.conectar() as conn:
        print("Conexión establecida con éxito.")

ahora()