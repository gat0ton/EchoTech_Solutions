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

    @staticmethod
    def _verificar_login(usualist):
        params= None
        if login(params) in list:
                return login
        else:
            return False
        
    @contextmanager
    def conectar(self):


        try:
            conexion = pymysql.connect(**self.__config)

            print(self.mensajesBDD('conexion_e'))

            yield conexion

        except Exception:
            self.rollback(conexion)

        finally:
            self.desconectar(conexion)



