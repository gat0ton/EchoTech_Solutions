from subprocess import run
from sys import exit
from Fuente.Logica.logica_i import Menu

def limpiar():
    run('cls')

class Logica:

    def principal(self):

        while True:

            try:


                limpiar()
                Menu._mensaje('login', 'menu')
                opcion = input(Menu._mensaje('aux','opcion'))


                if opcion.strip() == "1":

                    __usuario = input(Menu._mensaje('login','usuario'))
                    __contrasena = input(Menu._mensaje('login','contraseña'))

                    nombre_usuario = aut._verificar_login(__usuario, __contrasena)


                    if nombre_usuario is None:

                        Menu._mensaje('login','contraseña_invalida')
                        Menu.limpiar()

                    else:

                        Menu._mensaje('','',nombre_usuario)

                    
                else:

                    Menu._mensaje('aux','salir')
                    exit()


            except ValueError:

                Menu.limpiar()
                Menu._mensaje('aux','opcion_invalida')


    def usuario(nombre: str):
        while True:

            try:

                Menu.limpiar_pantalla()
                Menu._mensaje('login','bienvenida', nombre)

                opcion = input(Menu._mensaje('aux', 'opcion'))

                

                if opcion == "1":
                                    
                    break

                elif opcion == "2":
                    Menu._mensaje('usuario', 'proyectos')
                    break

                elif opcion == "3":
                    Menu._mensaje('usuario', 'actualizar')
                    break

                elif opcion == "4":
                    Menu._mensaje('aux', 'salir')
                    exit()

                else:
                    Menu._mensaje('aux', 'opcion_invalida')
                    Menu.limpiar_pantalla()

            except ValueError:
                Menu._mensaje('aux', 'opcion_invalida')
                Menu.limpiar_pantalla()

        

        

        
        


        
        
        
    


        
        
        
    
