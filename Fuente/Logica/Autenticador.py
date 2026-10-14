from ..Clase.Usuario import U_empleado as uemp
usrs = []
usrs.append(uemp)
#users.append(DAO) CAMBIAR!!!
class Autenticador:

    @staticmethod  
    def _verificar_login(__id, __contraseña, usuarios=usrs):
        for usuario in usuarios:
            if str(usuario.id_usuario) == str(__id) and usuario.contraseña == __contraseña:
                return usuario.nombre
        return None
    
    