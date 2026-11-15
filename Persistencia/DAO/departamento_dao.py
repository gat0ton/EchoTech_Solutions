from Persistencia.DAO.conexion import ConexionBD, ErrorPersistencia
from DTO.Administracion.departamento_dto import DepartamentoDTO
import pymysql


class DepartamentoDAO:

    def __init__(self, conexion: ConexionBD):
        if conexion is None:
            raise ValueError("DepartamentoDAO necesita una conexión existente.")
        self.conexion = conexion

    def agregar(self, departamento: DepartamentoDTO):
        try:
            with self.conexion.conectar() as conexion_activa:
                cursor = self.conexion.ejecuta_query(
                    conexion_activa,
                    """
                    INSERT INTO departamento (nombre, descripcion, responsable_id)
                    VALUES (%s, %s, %s)
                    """,
                    (departamento.nombre, departamento.descripcion, departamento.responsable_id),
                )
                try:
                    self.conexion.commit(conexion_activa)
                finally:
                    cursor.close()
            return departamento
        except pymysql.MySQLError as error:
            raise ErrorPersistencia("No fue posible registrar el departamento.") from error

    def actualizar(self, nombre, descripcion, responsable_id):
        try:
            with self.conexion.conectar() as conexion_activa:
                cursor = self.conexion.ejecuta_query(
                    conexion_activa,
                    """
                    UPDATE departamento
                    SET descripcion = %s, responsable_id = %s
                    WHERE nombre = %s
                    """,
                    (descripcion, responsable_id, nombre),
                )
                try:
                    self.conexion.commit(conexion_activa)
                finally:
                    cursor.close()
        except pymysql.MySQLError as error:
            raise ErrorPersistencia("No fue posible actualizar el departamento.") from error
