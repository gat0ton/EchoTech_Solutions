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
        return super()._consultar_datos()[0]

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

    
    def _actualizar_datos(
            self,
                         input_id: int, 
                         input_nombre: str, input_apellido: str, 
                         input_edad: int, input_telefono: str, 
                         input_direccion: str, input_puesto: str, input_horas: int, 
                         input_salario: float
                         
                         ):
        super()._actualizar_datos(
            input_id,
            input_nombre,
            input_apellido,
            input_edad,
            input_telefono,
            input_direccion,
            input_puesto,
            input_horas,
            input_salario,
        )
        self.__puesto = input_puesto
        self.__horas = input_horas
        self.__salario = input_salario

empleado = Empleado(1, "Tomás", "Pérez", 27, "555-1234", "Calle Falsa 123", "tomás.perez@example.com", "admin", 0, 1)