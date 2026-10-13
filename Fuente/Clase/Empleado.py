from .Persona import Persona as p

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

    
    @property
    def id_usuario(self):
        return self.__id

    def __consultar_datos(self):
        return {
            "ID": self.__id,
            "Nombre": self.__nombre,
            "Apellido": self.__apellido,
            "Edad": self.__edad,
            "Teléfono": self.__telefono,
            "Dirección": self.__direccion,
            "Puesto": self.__puesto,
            "Horas": self.__horas,
            "Salario": self.__salario
        }

    
    def __actualizar_datos(
            self,
                         input_id: int, 
                         input_nombre: str, input_apellido: str, 
                         input_edad: int, input_telefono: str, 
                         input_direccion: str, input_puesto: str, input_horas: int, 
                         input_salario: float
                         
                         ):
        
        self.__id = input_id
        self.__nombre = input_nombre
        self.__apellido = input_apellido
        self.__edad = input_edad
        self.__telefono = input_telefono
        self.__direccion = input_direccion
        self.__puesto = input_puesto
        self.__horas = input_horas
        self.__salario = input_salario

empleado = Empleado(1, "Tomás", "Pérez", 27, "555-1234", "Calle Falsa 123", "tomás.perez@example.com", "Desarrollador", 40, 50000.0)