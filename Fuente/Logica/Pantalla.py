from .Autenticador import Autenticador
from .Menu import Menu
from sys import exit

def principal(no_login: bool):
    while no_login:
        try:
            Menu.limpiar_pantalla()
            Menu.mostrar_mensaje('login', 'menu')
            opcion = input(Menu.mensaje('aux','opcion'))

            if opcion.strip() == "1":
                usuario = input(Menu.mensaje('login','usuario'))
                contraseña = input(Menu.mensaje('login','contraseña'))

                nombre_usuario = Autenticador._verificar_login(usuario, contraseña)
                if nombre_usuario is None:
                    Menu.mostrar_mensaje('login','contraseña_invalida')
                    Menu.limpiar_pantalla()
                else:
                    return nombre_usuario
            else:
                Menu.mostrar_mensaje('aux','salir')
                exit()
        except ValueError:
            Menu.limpiar_pantalla()
            Menu.mostrar_mensaje('aux','opcion_invalida')

def usuario(no_admin: bool, nombre: str):
    while no_admin:
        try:
            Menu.limpiar_pantalla()
            Menu.mostrar_mensaje('login','bienvenida', nombre)
            Menu.mostrar_mensaje('usuario','menu')

            opcion = input(Menu.mensaje('aux', 'opcion'))

            if opcion == "1":
                                
                break

            elif opcion == "2":
                Menu.mostrar_mensaje('usuario', 'proyectos')
                break

            elif opcion == "3":
                Menu.mostrar_mensaje('usuario', 'actualizar')
                break

            elif opcion == "4":
                Menu.mostrar_mensaje('aux', 'salir')
                exit()

            else:
                Menu.mostrar_mensaje('aux', 'opcion_invalida')
                Menu.limpiar_pantalla()

        except ValueError:
            Menu.mostrar_mensaje('aux', 'opcion_invalida')
            Menu.limpiar_pantalla()