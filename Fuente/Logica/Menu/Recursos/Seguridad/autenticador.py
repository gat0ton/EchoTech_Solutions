from DTO.gestor_dto import Repositorio as rep

class Autenticador:
    @staticmethod
    def __login(id, contrasena):
        if id and contrasena in rep._listas():
            return True
