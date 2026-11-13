from DAO.usuario_dao import UsuarioDAO
class Autenticador:

    ROL_ADMIN = "admin"
    LARGO_MINIMO_CONTRASENA = 8

    def existe_admin(self):
        return self.usuario_dao.existeRol(self.ROL_ADMIN)
    
    def __init__(self, usuario_dao: UsuarioDAO):
        self.usuario_dao = usuario_dao

    def login(self, user: str, contrasena: str):
        if user and contrasena:
            return self.usuario_dao.rol_registrado(user, contrasena)