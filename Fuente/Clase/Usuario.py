from .Empleado import Empleado 
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

    def _mostrar_informacion(self):
        return {
            "ID": self.__id,
            "Nombre": self.__nombre,
            "Contraseña": self.__contraseña
        }

    
    @property
    def id_usuario(self):
        return self.__id

@property
def contraseña(self):
    return self.__contraseña

U_empleado = Usuario(empleado.__id, empleado.__nombre, "123")
print(U_empleado._mostrar_informacion())