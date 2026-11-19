from Persistencia.DAO.conexion import ConexionBD, ErrorPersistencia
from DTO.Administracion.proyecto_dto import ProyectoDTO
import pymysql


class ProyectoDAO:
    def __init__(self, conexion: ConexionBD):
        if conexion is None:
            raise ValueError("ProyectoDAO necesita una conexión existente.")
        self.conexion = conexion

    def agregar(self, proyecto: ProyectoDTO):
        try:
            with self.conexion.conectar() as conexion_activa:
                registro_cursor = self.conexion.ejecuta_query(
                    conexion_activa,
                    """
                    INSERT INTO registro (horas, fecha, id_asociado)
                    VALUES (%s, %s, %s)
                    """,
                    (
                        proyecto.registro_horas,
                        proyecto.registro_fecha,
                        proyecto.registro_id_asociado,
                    ),
                )
                try:
                    registro_id = registro_cursor.lastrowid
                finally:
                    registro_cursor.close()

                proyecto_cursor = self.conexion.ejecuta_query(
                    conexion_activa,
                    """
                    INSERT INTO proyecto
                    (nombre, departamento_nombre, registro_id, pais,
                     presupuesto_clp, moneda, presupuesto_local, tasa_conversion)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """,
                    (
                        proyecto.nombre,
                        proyecto.departamento_nombre,
                        registro_id,
                        proyecto.pais,
                        proyecto.presupuesto_clp,
                        proyecto.moneda,
                        proyecto.presupuesto_local,
                        proyecto.tasa_conversion,
                    ),
                )
                try:
                    proyecto_id = proyecto_cursor.lastrowid
                finally:
                    proyecto_cursor.close()
                relacion_cursor = self.conexion.ejecuta_query(
                    conexion_activa,
                    """
                    INSERT INTO proyecto_registro (proyecto_id, registro_id)
                    VALUES (%s, %s)
                    """,
                    (proyecto_id, registro_id),
                )
                relacion_cursor.close()
                self.conexion.commit(conexion_activa)

            return proyecto_id
        except pymysql.MySQLError as error:
            raise ErrorPersistencia("No fue posible registrar el proyecto.") from error

    def buscar_detalle(self, proyecto_id):
        try:
            with self.conexion.conectar() as conexion_activa:
                cursor = self.conexion.ejecuta_query(
                    conexion_activa,
                    """
                    SELECT p.id, p.nombre, p.pais, p.presupuesto_clp,
                           p.moneda, p.presupuesto_local, p.departamento_nombre,
                           e.id, e.nombre, e.apellido, e.puesto
                    FROM proyecto p
                    LEFT JOIN proyecto_empleado pe ON pe.proyecto_id = p.id
                    LEFT JOIN empleado e ON e.id = pe.empleado_id
                    WHERE p.id = %s
                    """,
                    (proyecto_id,),
                )
                try:
                    filas = cursor.fetchall()
                finally:
                    cursor.close()
        except pymysql.MySQLError as error:
            raise ErrorPersistencia("No fue posible consultar el proyecto.") from error

        if not filas:
            return None

        proyecto = {
            "id": filas[0][0],
            "nombre": filas[0][1],
            "pais": filas[0][2],
            "presupuesto_clp": filas[0][3],
            "moneda": filas[0][4],
            "presupuesto_local": filas[0][5],
            "departamento": filas[0][6],
            "empleados": [],
        }
        for fila in filas:
            if fila[7] is not None:
                proyecto["empleados"].append(
                    {
                        "id": fila[7],
                        "nombre": f"{fila[8]} {fila[9]}",
                        "puesto": fila[10],
                    }
                )
        return proyecto

    def historial_registros(self, proyecto_id):
        try:
            with self.conexion.conectar() as conexion_activa:
                cursor = self.conexion.ejecuta_query(
                    conexion_activa,
                    """
                    SELECT r.id, r.horas, r.fecha, r.id_asociado
                    FROM registro r
                    INNER JOIN proyecto_registro pr ON pr.registro_id = r.id
                    WHERE pr.proyecto_id = %s
                    ORDER BY r.fecha DESC, r.id DESC
                    """,
                    (proyecto_id,),
                )
                try:
                    filas = cursor.fetchall()
                finally:
                    cursor.close()
        except pymysql.MySQLError as error:
            raise ErrorPersistencia("No fue posible consultar el historial del proyecto.") from error
        return [
            {
                "id": fila[0],
                "horas": fila[1],
                "fecha": fila[2],
                "id_asociado": fila[3],
            }
            for fila in filas
        ]

    def asociar_empleado(self, proyecto_id, empleado_id):
        try:
            with self.conexion.conectar() as conexion_activa:
                cursor = self.conexion.ejecuta_query(
                    conexion_activa,
                    """
                    INSERT INTO proyecto_empleado (proyecto_id, empleado_id)
                    VALUES (%s, %s)
                    """,
                    (proyecto_id, empleado_id),
                )
                try:
                    self.conexion.commit(conexion_activa)
                finally:
                    cursor.close()
        except pymysql.MySQLError as error:
            raise ErrorPersistencia("No fue posible asociar el empleado al proyecto.") from error
