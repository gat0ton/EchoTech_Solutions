from ..Clase.Usuario import Usuario
from ..Clase.Usuario import U_empleado as uemp
from . import Salida
usuarios = [Usuario, uemp]
#users.append(DAO) CAMBIAR!!!
class Autenticador:

    @staticmethod
    def _verificar_login(__id, __contraseña, usuarios):
        no_login = True
        for usuario in usuarios:
            if usuario.__id == __id and usuario.__contraseña == __contraseña:
                
                Salida.limpiar_pantalla()
                print(f"Bienvenido, {usuario.__id}!")

                return no_login == False
            
        return no_login == True