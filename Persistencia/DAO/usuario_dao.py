from Persistencia.DAO.conexion import ConexionBD, ErrorPersistencia
from DTO.usuario_dto import UsuarioDTO
import pymysql

class UsuarioDAO:

    def __init__(self, conexion: ConexionBD):
        if conexion is None:
            raise ValueError("UsuarioDAO necesita una conexión existente.")
        self.conexion = conexion

    def agregar(self, usuario_dto):
        try:
            with self.conexion.conectar() as conexion_activa:                           
                cursor = self.conexion.ejecuta_query(                                   
                    conexion_activa,
                    "INSERT INTO usuario (username, passwordHash, rol) VALUES (%s, %s, %s)",
                    (usuario_dto.username, usuario_dto.passwordHash, usuario_dto.rol),
                )
                try:
                    self.conexion.commit(conexion_activa)                               
                    usuario_dto.numUsuario = cursor.lastrowid
                finally:
                    cursor.close()
            return usuario_dto                                                           
        except pymysql.MySQLError as error:
            raise ErrorPersistencia("No fue posible registrar el usuario.") from error

    def buscar_por_username(self, username):
        try:
            with self.conexion.conectar() as conexion_activa:                           
                cursor = self.conexion.ejecuta_query(                                   
                    conexion_activa,
                    "SELECT numUsuario, username, passwordHash, rol FROM usuario WHERE username = %s",
                    (username,),
                )
                try:
                    fila = cursor.fetchone()   
                finally:
                    cursor.close()
        except pymysql.MySQLError as error:
            raise ErrorPersistencia("No fue posible consultar el usuario.") from error

        if fila is None:
            return None
        return UsuarioDTO(*fila)

    def actualizar_password(self, username, passwordHash):
        try:
            with self.conexion.conectar() as conexion_activa:                           
                cursor = self.conexion.ejecuta_query(                                   
                    conexion_activa,
                    "UPDATE usuario SET passwordHash = %s WHERE username = %s",
                    (passwordHash, username),
                )
                try:
                    self.conexion.commit(conexion_activa)                               
                finally:
                    cursor.close()
        except pymysql.MySQLError as error:
            raise ErrorPersistencia("No fue posible actualizar la contraseña.") from error

    def actualizar_username(self, username, nuevo_username):
        try:
            with self.conexion.conectar() as conexion_activa:
                cursor = self.conexion.ejecuta_query(
                    conexion_activa,
                    "UPDATE usuario SET username = %s WHERE username = %s",
                    (nuevo_username, username),
                )
                try:
                    self.conexion.commit(conexion_activa)
                finally:
                    cursor.close()
        except pymysql.MySQLError as error:
            raise ErrorPersistencia("No fue posible actualizar el nombre de usuario.") from error

    def existe_rol(self, rol):
        try:
            with self.conexion.conectar() as conexion_activa:                           
                cursor = self.conexion.ejecuta_query(                                   
                    conexion_activa,
                    "SELECT 1 FROM usuario WHERE rol = %s LIMIT 1",
                    (rol,),
                )
                try:
                    return cursor.fetchone() is not None
                finally:
                    cursor.close()
        except pymysql.MySQLError as error:
            raise ErrorPersistencia("No fue posible consultar los usuarios.") from error
