from .Empleado import empleado #CAMBIAR!!!

class Usuario:

    def __init__(
            self,
                __id: int,
                __nombre: str,
                   __contraseña: str
                   ):
        self.__id = __id
        self.__nombre = __nombre
        self.__contraseña = __contraseña
    
    @property
    def id_usuario(self):
        return self.__id

    @property
    def contraseña(self):
        return self.__contraseña
    
    @property
    def nombre(self):
        return self.__nombre
SUPER_ADMIN = Usuario(empleado.id_usuario, empleado._consultar_datos()["Nombre"], "123")
    
