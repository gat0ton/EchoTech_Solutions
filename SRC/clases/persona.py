from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(
        self,
        numeroPersona: int,
        nombre: str,
        apellido: str,
        telefono: str,
        correo: str,
        direccion: str,
        contraseña: str,
        inicioContrato: str,
        sueldo: float,
    ):
        
            self._numeroPersona = numeroPersona
            self._nombre = nombre
            self._apellido = apellido
            self._telefono = telefono
            self._correo = correo
            self._direccion = direccion
            self._contraseña = contraseña
            self._inicioContrato = inicioContrato
            self._sueldo = sueldo


    @abstractmethod
    def consultarDatos(self):
        pass

    @abstractmethod
    def iniciarSesion(self, correo, contraseña):
        pass

    @abstractmethod
    def cambiarContraseña(self, nuevaContraseña):
        pass