from Presentación.login import Login
from Persistencia.DAO.conexion import ConexionBD
from Persistencia.DAO.usuario_dao import UsuarioDAO
from Presentación.menu_principal import MenuPrincipal
from Negocio.Servicios.servicios_autenticacion import ServicioAutenticacion

class Flujo:
    def main():

        try:
            conexion = ConexionBD()
        except ValueError as error:
            print(f"Error: {error}")
            return

        # Persistencia → Negocio → Presentación: cada capa recibe la que está debajo (inyección de dependencias).
        usuario_dao = UsuarioDAO(conexion)
        servicio_autenticacion = ServicioAutenticacion(usuario_dao)
        login = Login(servicio_autenticacion)

        # Si todavía no hay administrador (instalación nueva), se pide crearlo antes del inicio de sesión.
        try:
            hayAdministrador = servicio_autenticacion.existeAdministrador()
        # ErrorPersistencia hereda de RuntimeError.
        except RuntimeError:
            print("Error al acceder a la base de datos. Revise la configuración del archivo .env.")
            return

        if not hayAdministrador and not login.crearPrimerAdministrador():
            print("\nNo es posible usar el sistema sin un administrador. Saliendo...")
            return

        # Al cerrar sesión se vuelve al inicio de sesión para que otra persona pueda entrar.
        # El programa termina si se cancela el login, se agotan los intentos o falla la base de datos.
        while True:
            usuario = login.iniciarSesion()

            if usuario is None:
                print("\nSaliendo del sistema...")
                break

            MenuPrincipal(usuario, servicio_autenticacion).mostrarMenu()

