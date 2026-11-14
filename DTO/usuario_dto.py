class UsuarioDTO:

    def __init__(self, numUsuario, username, passwordHash, rol, id_empleado=None):
        self.numUsuario = numUsuario
        self.username = username
        self.passwordHash = passwordHash
        self.rol = rol
        self.id_empleado = id_empleado