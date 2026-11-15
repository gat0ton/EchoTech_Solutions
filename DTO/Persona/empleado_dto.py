class EmpleadoDTO:
    def __init__(self, _id: int, _nombre: str, _apellido: str, _edad: int, _genero: str, _telefono: str, _direccion: str,
                        _correo: str,
                        _horas: int,
                        _salario: float,
                        puesto: str
                     ):
        self.id = _id
        self.nombre = _nombre
        self.apellido = _apellido
        self.edad = _edad
        self.genero = _genero
        self.telefono = _telefono
        self.direccion = _direccion
        self.correo = _correo
        self.horas = _horas
        self.salario = _salario
        self.puesto = puesto