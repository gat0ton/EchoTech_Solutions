from .persona import Persona as p

class Empleado(p):
    def __init__(
                self, 
                    __id: int, 
                    __nombre: str, 
                    __apellido: str, 
                    __edad: int, 
                    __telefono: str, 
                    __direccion: str,
                    __correo: str,
                    __puesto: str,
                    __horas: int,
                    __salario: float
                 
                 ):
        
        super().__init__(__id, __nombre, __apellido, __edad, __telefono, __direccion, __correo)
        
        self.__puesto = __puesto
        self.__horas = __horas
        self.__salario = __salario
        
    def _consultar_datos(self):
        id_, nombre, apellido, edad, telefono, direccion, correo = super()._consultar_datos()
        return {
            "ID": id_,
            "Nombre": nombre,
            "Apellido": apellido,
            "Edad": edad,
            "Teléfono": telefono,
            "Dirección": direccion,
            "Correo": correo,
            "Puesto": self.__puesto,
            "Horas": self.__horas,
            "Salario": self.__salario
        }