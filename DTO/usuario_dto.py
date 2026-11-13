class UsuarioDTO:

    def __init__(self, numUsuario, username, hashedPassword, rol, id_empleado=None):
        self.numUsuario = numUsuario
        self.username = username
        self.hashedPassword = hashedPassword
        self.rol = rol
        self.id_empleado = id_empleado