from Persona.empleado import Empleado 

class Usuario:

    def __init__(
            self,
                id: int,
                nombre: str,
                   contrasena: str):
        
        self.__id = id
        self.__nombre = nombre
        self.__contrasena = contrasena
    
    def _registro(self):
        return (
            self.__id,
            self.__nombre,
            self.__contrasena)
    
    

