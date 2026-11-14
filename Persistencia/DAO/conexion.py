from contextlib import contextmanager
from dotenv import load_dotenv
from pathlib import Path
import pymysql
import os

class ErrorPersistencia(RuntimeError):
    """Error seguro para comunicar fallos de operaciones con la BD."""

class ConexionBD:
    def __init__(self):
        load_dotenv(Path(__file__).resolve().parents[2] / ".env", override=True)

        host = os.getenv("DB_HOST")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        database = os.getenv("DB_NAME")
        port = os.getenv("DB_PORT")

        if not host or not user or password is None or not database:
            raise ValueError("La configuración de la base de datos está incompleta.")
        try:
            port = int(port or "3306")
        except ValueError as error:
            raise ValueError("El puerto de la base de datos no es válido.") from error

        self.config = {
            "host": host,
            "user": user,
            "password": password,
            "database": database,
            "port": port,
            "autocommit": False,
        }

    @contextmanager
    def conectar(self):
        conexionBD = None
        try:
            conexionBD = pymysql.connect(**self.config)
            yield conexionBD 
        except Exception:
            if conexionBD is not None:
                self.rollback(conexionBD)
            raise
        finally:
            if conexionBD is not None:
                self.desconectar(conexionBD)

    def ejecuta_query(self, conexionBD, sql, params=None):
        cursor = conexionBD.cursor()
        if params is None:
            cursor.execute(sql)
        else:
            cursor.execute(sql, params)
        return cursor

    def commit(self, conexionBD):
        conexionBD.commit()

    def rollback(self, conexionBD):
        conexionBD.rollback()

    def desconectar(self, conexionBD):
        conexionBD.close()