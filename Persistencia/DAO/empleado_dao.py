from Persistencia.DAO.conexion import ConexionBD, ErrorPersistencia
from DTO.Persona.empleado_dto import EmpleadoDTO
import pymysql


class EmpleadoDAO:

    def __init__(self, conexion: ConexionBD):
        if conexion is None:
            raise ValueError("EmpleadoDAO necesita una conexión existente.")
        self.conexion = conexion

    def agregar(self, empleado_dto: EmpleadoDTO):
        try:
            with self.conexion.conectar() as conexion_activa:
                cursor = self.conexion.ejecuta_query(
                    conexion_activa,
                    """
                    INSERT INTO empleado
                    (id, nombre, apellido, edad, genero, telefono, direccion,
                     correo, horas, salario, puesto, username, departamento)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """,
                    (
                        empleado_dto.id,
                        empleado_dto.nombre,
                        empleado_dto.apellido,
                        empleado_dto.edad,
                        empleado_dto.genero,
                        empleado_dto.telefono,
                        empleado_dto.direccion,
                        empleado_dto.correo,
                        empleado_dto.horas,
                        empleado_dto.salario,
                        empleado_dto.puesto,
                        empleado_dto.username,
                        empleado_dto.departamento,
                    ),
                )
                try:
                    self.conexion.commit(conexion_activa)
                finally:
                    cursor.close()
            return empleado_dto
        except pymysql.MySQLError as error:
            raise ErrorPersistencia("No fue posible registrar el empleado.") from error

    def buscarPorUsername(self, username):
        try:
            with self.conexion.conectar() as conexion_activa:
                cursor = self.conexion.ejecuta_query(
                    conexion_activa,
                    """
                    SELECT id, nombre, apellido, edad, genero, telefono, direccion,
                           correo, horas, salario, puesto, username, departamento
                    FROM empleado
                    WHERE username = %s
                    """,
                    (username,),
                )
                try:
                    fila = cursor.fetchone()
                finally:
                    cursor.close()
        except pymysql.MySQLError as error:
            raise ErrorPersistencia("No fue posible consultar el empleado.") from error

        return None if fila is None else EmpleadoDTO(*fila)

    def actualizarContacto(self, username, nuevo_username, telefono, direccion, correo):
        try:
            with self.conexion.conectar() as conexion_activa:
                cursor = self.conexion.ejecuta_query(
                    conexion_activa,
                    """
                    UPDATE empleado
                    SET username = %s, telefono = %s, direccion = %s, correo = %s
                    WHERE username = %s
                    """,
                    (nuevo_username, telefono, direccion, correo, username),
                )
                try:
                    self.conexion.commit(conexion_activa)
                finally:
                    cursor.close()
        except pymysql.MySQLError as error:
            raise ErrorPersistencia("No fue posible actualizar el empleado.") from error

    def buscarPorId(self, empleado_id):
        try:
            with self.conexion.conectar() as conexion_activa:
                cursor = self.conexion.ejecuta_query(
                    conexion_activa,
                    "SELECT id, puesto FROM empleado WHERE id = %s",
                    (empleado_id,),
                )
                try:
                    fila = cursor.fetchone()
                finally:
                    cursor.close()
        except pymysql.MySQLError as error:
            raise ErrorPersistencia("No fue posible consultar el empleado.") from error
        return fila
