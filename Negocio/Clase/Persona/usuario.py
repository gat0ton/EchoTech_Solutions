class Usuario:

    def __init__(
            self,
                user: str,
                nombre: str,
                rol: str,
                contrasena: str):
        
        self.__user = user
        self.__nombre = nombre
        self.__rol = rol
        self.__contrasena = contrasena
    
    def _registro(self):
        return (
            self.__user,
            self.__nombre,
            self.__rol,
            self.__contrasena)

    def __str__(self):
        return f"""
        {'-'* 40}
        Usuario: {self.__nombre}
        ID: {self.__id}
        {'-'* 40}"""
    
    

