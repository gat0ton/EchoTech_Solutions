from persona import Persona

class Empleado(Persona):
    def __init__(self, 
                    numeroPersona: int,
                    nombre: str, 
                    apellido: str, 
                    telefono: str, 
                    correo: str, 
                    direccion: str, 
                    contraseña: str,
                    inicioContrato: str,
                    sueldo: float,
                    cargo: str
                    ):

        super().__init__(
                    numeroPersona,
                    nombre,
                    apellido,
                    telefono,
                    correo,
                    direccion,
                    contraseña,
                    inicioContrato,
                    sueldo
                )   
        self._cargo = cargo

        

    def consultarDatos(self):
        return (
            f"N° Persona: {self._numeroPersona}"
            f"Nombre: {self._nombre}"
            f"Apellido: {self._apellido}"
            f"Teléfono: {self._telefono}"
            f"Correo: {self._correo}"
            f"Dirección: {self._direccion}"
            f"Inicio Contrato: {self._inicioContrato}"
            f"Sueldo: {self._sueldo}"
        )

    def iniciarSesion(self, correo, contraseña):
        if self._correo == correo and self._contraseña == contraseña:
            return True
        return False

    def cambiarContraseña(self, nuevaContraseña):
        self._contraseña = nuevaContraseña
        return True

    def registrarHoras(self, fechaRegistro, cantidadHoras, descripcion, proyecto):
        pass #Se heredarán parametros desde clase Registro.
