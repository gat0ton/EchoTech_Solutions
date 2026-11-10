class Usuario:

    def __init__(
            self,
                id: int,
                nombre: str,
                   contrasena: str):
        
        self.__id = id
        self.__nombre = nombre
        self.__contrasena = contrasena
    
    def _registro(self):
        return (
            self.__id,
            self.__nombre,
            self.__contrasena)

    def __str__(self):
        return f"""
        {'-'* 40}
        Usuario: {self.__nombre}
        ID: {self.__id}
        {'-'* 40}"""
    
    

