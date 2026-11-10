from dotenv import load_dotenv
from contextlib import contextmanager
from pathlib import Path
import os
import pymysql

class Conexion:
    def __init__(self):

        load_dotenv(
            Path(__file__).resolve().parents[2] / '.env'
                    )

        
        # Agrupamos todos los parámetros desde el archivo de configuracion (.env) en un diccionario de configuración
        self.config = {
            "host": os.getenv("DB_HOST"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "database": os.getenv("DB_NAME"),      
            "port": os.getenv("DB_PORT"),
            "autocommit": False  
        }

        if (not self.config["host"] or not self.config["user"] or self.config["password"] is None or not self.config["database"]):
            raise ValueError("La configuración está incompleta. Por favor, revisa .env")
        try:
            int(self.config["port"] or "3306")#Transforma el puerto a entero, o lo deja por defecto (3306)
        except ValueError as error:
            raise ValueError("No se ha podidio validar el puerto.") from error

        
    @contextmanager
    def conectar(self):
        conexion = None
        try:
            conexion = pymysql.connect(**self.__config)

            yield conexion
        
        except Exception:
            self.rollback(conexion)

        finally:
            self.desconectar(conexion)

    def ejecutar_query(self, conexion, sql, params=None):
        cursor = conexion.cursor()
        if params is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, params)
        return cursor

    def commit(self, conexion):
        conexion.commit()

    def rollback(self, conexion):
            conexion.rollback()