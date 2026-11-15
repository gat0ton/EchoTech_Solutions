from Presentación.login import Login
from Persistencia.DAO.conexion import ConexionBD
from Persistencia.DAO.usuario_dao import UsuarioDAO
from Persistencia.DAO.empleado_dao import EmpleadoDAO
from Presentación.menu_principal import MenuPrincipal
from Negocio.Servicios.servicios_autenticacion import ServicioAutenticacion

class Flujo:
    def main():

        try:
            conexion = ConexionBD()
        except ValueError as error:
            print(f"Error: {error}")
            return

        usuario_dao = UsuarioDAO(conexion)
        empleado_dao = EmpleadoDAO(conexion)
        servicio_autenticacion = ServicioAutenticacion(usuario_dao, empleado_dao)
        login = Login(servicio_autenticacion)

        try:
            hayAdministrador = servicio_autenticacion.existeAdministrador()
        except RuntimeError:
            print("Error al acceder a la base de datos. Revise la configuración del archivo .env.")
            return

        if not hayAdministrador and not login.crearPrimerAdministrador():
            print("\nNo es posible usar el sistema sin un administrador. Saliendo...")
            return

        
        while True:
            usuario = login.iniciarSesion()

            if usuario is None:
                print("\nSaliendo del sistema...")
                break

            MenuPrincipal(usuario, servicio_autenticacion).mostrarMenu()

