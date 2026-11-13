from Fuente.Persistencia.conexion import Conexion, ErrorPersistencia
from DTO.usuario_dto import UsuarioDTO
import pymysql

class UsuarioDAO:
    def __init__(self, conexion: Conexion):

        self.conexion = conexion
        if conexion is None:
            raise ValueError("Debe haber un parámetro de conexión válido para inicializar UsuarioDAO.")

    def agregar(self, usuario_dto):
        try:
            with self.conexion.conectar() as conexion_activa:                           # 1. Conectar
                cursor = self.conexion.ejecuta_query(                                    # 2. Cursor y query
                    conexion_activa,
                    "INSERT INTO usuario (username, passwordHash, rol) VALUES (%s, %s, %s)",
                    (usuario_dto.username, usuario_dto.passwordHash, usuario_dto.rol),
                )
                try:
                    self.conexion.commit(conexion_activa)                                # 3. Commit
                    usuario_dto.numUsuario = cursor.lastrowid
                finally:
                    cursor.close()
            return usuario_dto                                                           # 4. Cerrada al salir del with
        except pymysql.MySQLError as error:
            raise ErrorPersistencia("No fue posible registrar el usuario.") from error

    def buscar_por_username(self, username):
        try:
            with self.conexion.conectar() as conexion_activa:                           # 1. Conectar
                cursor = self.conexion.ejecuta_query(                                    # 2. Cursor y query
                    conexion_activa,
                    "SELECT numUsuario, username, passwordHash, rol FROM usuario WHERE username = %s",
                    (username,),
                )
                try:
                    fila = cursor.fetchone()   # Una consulta SELECT no modifica datos: no necesita commit.
                finally:
                    cursor.close()
        except pymysql.MySQLError as error:
            raise ErrorPersistencia("No fue posible consultar el usuario.") from error

        if fila is None:
            return None
        return UsuarioDTO(*fila)

    def rol_registrado(self, rol):

        try:
            with self.conexion.conectar() as conexion_activa:
                cursor = self.conexion.ejecutar_query(
                    conexion_activa, "SELECT 1 FROM usuario WHERE rol = %s LIMIT 1",
                    (rol)
                    )
                try:
                    cursor.fetchone() is not None

                finally:
                    cursor.close()
        except  pymysql.MySQLError as error:
            print(f"Error al verificar el rol registrado: {error}")
            return False
            
