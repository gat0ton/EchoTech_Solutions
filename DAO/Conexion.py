import pymysql
from contextlib import contextmanager

class Conexion:

    

    def __init__(self):

        config = {
                            'host'       : 'localhost',
                            'port'       : int(3306),
                            'user'       : 'admin',
                            'password'   : '',
                            'database'   : 'EchoTech Solutions',
                            'autocommit' : False
                        }

        self.__config = config

    @contextmanager
    def conectar(self):
        conexion = pymysql.connect(**self.__config)
        print(self.mensajesBDD('conexion_e'))
        try:
            yield conexion
        except Exception:
            self.rollback(conexion)
        finally:
            self.desconectar(conexion)



