from .Autenticador import Autenticador
from .Menu import Menu
from sys import exit

no_login = True
no_admin = True
def principal():
    while no_login:
        try:
            
            opcion = input(Menu.mensaje('aux','opcion'))

            if opcion.strip() == "1":
                usuario = input(Menu.mensaje('login','usuario'))
                contraseña = input(Menu.mensaje('login','contraseña'))

                if Autenticador._verificar_login(usuario, contraseña):

                    Menu.mensaje('login','contraseña_invalida')
                    Menu.limpiar_pantalla()
                    Menu.login()


                else:
                    break
                    
            else:
                Menu.salir()
                exit()
        except ValueError:
            Menu.invalido()
            Menu.limpiar_pantalla()    

while no_admin:
    try:
        Menu.limpiar_pantalla()
        Menu.usuario()

        opcion = input(Menu.opcion())

        if opcion == "1":
            print("Registrar Horas")            
            break

        elif opcion == "2":
            print("Consultar tus Proyectos")
            break

        elif opcion == "3":
            print("Actualizar tus Datos")
            break

        elif opcion == "4":
            Menu.salir()
            exit()

        else:
            print("Opción no válida, por favor intente de nuevo.")
            Menu.limpiar_pantalla()

    except ValueError:
        print("Opción no válida, por favor intente de nuevo.")
        Menu.limpiar_pantalla()