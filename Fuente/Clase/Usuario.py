from empleado import Empleado 

class Usuario:

    def __init__(
            self,
                __id: int,
                __nombre: str,
                   __contrasena: str
                   ):
        self.__id = __id
        self.__nombre = __nombre
        self.__contrasena = __contrasena
    
    @property
    def _registro(self):
        return self.__contraseña
    
    

_SUPER_ADMIN = (Usuario(Empleado(1,'','',1,'','',''),'admin','admin'))