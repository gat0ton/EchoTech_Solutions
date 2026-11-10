from conexion import Conexion
import pymysql

class UsuarioDAO:
    def __init__(self, conexion: Conexion):

        self.conexion = conexion
        if conexion is None:
            raise ValueError("Debe haber un parámetro de conexión válido para inicializar UsuarioDAO.")

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
            
