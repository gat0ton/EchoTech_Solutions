from .Autenticador import Autenticador
from .Salida import Salida
from sys import exit

no_login = True
no_admin = True
def principal():
    while no_login:
        try:
            
            opcion = input(Salida.mensaje('aux','opcion'))

            if opcion.strip() == "1":
                usuario = input(Salida.mensaje('login','usuario'))
                contraseña = input(Salida.mensaje('login','contraseña'))

                if Autenticador._verificar_login(usuario, contraseña):

                    Salida.mensaje('login','contraseña_invalida')
                    Salida.limpiar_pantalla()
                    Salida.login()


                else:
                    break
                    
            else:
                Salida.salir()
                exit()
        except ValueError:
            Salida.invalido()
            Salida.limpiar_pantalla()    

while no_admin:
    try:
        Salida.limpiar_pantalla()
        Salida.usuario()

        opcion = input(Salida.opcion())

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
            Salida.salir()
            exit()

        else:
            print("Opción no válida, por favor intente de nuevo.")
            Salida.limpiar_pantalla()

    except ValueError:
        print("Opción no válida, por favor intente de nuevo.")
        Salida.limpiar_pantalla()