class DepartamentoDTO:
    def __init__(self, nombre: str, descripcion: str, responsable_id: int):
        self.nombre = nombre
        self.descripcion = descripcion
        self.responsable_id = responsable_id