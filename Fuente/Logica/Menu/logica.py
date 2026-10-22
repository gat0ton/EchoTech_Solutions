lazy from sys import exit
from Fuente.Logica.Menu.Recursos.menu import Mensaje, Utilidades
lazy from Fuente.Logica.Menu.Recursos.Seguridad.autenticador import Autenticador

class Logica:
    def principal():

        while True:
            try:
                Utilidades._limpiar()
                print(Mensaje._mostrar(clave='login', nido='menu'))
                opcion = input(Mensaje._mostrar('aux','opcion'))
                Utilidades._limpiar()

                if opcion.strip() == "1":
                    __usuario = input(Mensaje._mostrar('login','usuario'))
                    __contrasena = input(Mensaje._mostrar('login','contraseña'))

                    if Autenticador.__login(__usuario, __contrasena):
                        break

                else:
                    Utilidades.salir()
                    exit()

            except ValueError:
                Utilidades._limpiar()
                Mensaje._mostrar('aux','opcion_invalida')

    def usuario(nombre: str):
        while True:
            try:
                Utilidades._limpiar()
                Mensaje._mostrar(nombre="tomas",genero='M')

                opcion = input(Mensaje._mostrar('aux', 'opcion'))

                if opcion == "1":
                    break

                elif opcion == "2":
                    Mensaje._mostrar('usuario', 'proyectos')
                    break

                elif opcion == "3":
                    Mensaje._mostrar('usuario', 'actualizar')
                    break

                elif opcion == "4":
                    Mensaje._mostrar('aux', 'salir')
                    exit()

                else:
                    Mensaje._mostrar('aux', 'opcion_invalida')
                    Utilidades._limpiar()

            except ValueError:
                Mensaje._mostrar('aux', 'opcion_invalida')
                Utilidades._limpiar()

        

        

        
        


        
        
        
    


        
        
        
    
