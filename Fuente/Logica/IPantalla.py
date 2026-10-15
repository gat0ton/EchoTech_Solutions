from os import system
from sys import exit
from .Autenticador import Autenticador as aut
from Fuente.Logica.IPantalla import IPantalla


class IPantalla:

    
    separar     = f'\n{"=" * 40}'
    
    advertencia = f'\n{"!" * 40}\n'

    __diccionario = {
                 
                'aux': {
                    'opcion'          : "Ingrese una Opcion: ",
                    
                    'valor'           : "Ingrese un Valor: ",
                    
                    'invalido'        : "Opción Invalida, por favor vuelve a Intentarlo.",
                    
                    'salir'           : "Saliendo del programa...",
                    
                    'opcion_invalida' : advertencia +
                                        """Opción no válida, por favor intente de nuevo.
                                        """  + advertencia},
    
    
                'login': {
                    'menu': separar +
                    
                    "Bienvenido al menú principal\n1. Iniciar Sesión\n2. Salir\n{separar}\n",
    
                    'id': "Ingresa tu ID de empleado: ",
                    
                    'usuario': "Ingresa tu ID de empleado: ",
                    
                    'contraseña': "Ingresa tu contraseña: ",
                    
                    'contraseña_invalida': "Contraseña o ID invalidos, por favor vuelve a intentarlo."},
    
    
                'usuario' : {

                    'menu': separar +

                    "1.- Registrar Horas"  +
    
                    "\n2.- Consultar tus Proyectos" +
    
                    "\n3.- Actualizar tus Datos" +
    
                    "\n4.- Salir" +

                    "\nConsultar tus Proyectos" +

                    separar},
    
    
                'conexion' : {
                    
                    'conexion_e' : "Conexión con Base de Datos Exitosa!",
                    
                    'conexion_f': "Conexión Fallida, intentalo mas tarde."},
    
    
                'registro' :{

                    'opcion' : "Horas Trabajadas: "}}

    def principal(no_login = True):
        while no_login:

            try:

                IPantalla.limpiar_pantalla()
                IPantalla.mensaje('login', 'menu')
                opcion = input(IPantalla.mensaje('aux','opcion'))


                if opcion.strip() == "1":

                    __usuario = input(IPantalla.mensaje('login','usuario'))
                    __contrasena = input(IPantalla.mensaje('login','contraseña'))

                    nombre_usuario = aut._verificar_login(__usuario, __contrasena)


                    if nombre_usuario is None:

                        IPantalla.mensaje('login','contraseña_invalida')
                        IPantalla.limpiar_pantalla()

                    else:

                        return nombre_usuario

                    
                else:

                    IPantalla.mensaje('aux','salir')
                    exit()


            except ValueError:

                IPantalla.limpiar_pantalla()
                IPantalla.mensaje('aux','opcion_invalida')


    def usuario(no_admin: bool, nombre: str):
        while no_admin:

            try:

                IPantalla.limpiar_pantalla()
                IPantalla.mensaje('login','bienvenida', nombre)

                opcion = input(IPantalla.mensaje('aux', 'opcion'))

                

                if opcion == "1":
                                    
                    break

                elif opcion == "2":
                    IPantalla.mensaje('usuario', 'proyectos')
                    break

                elif opcion == "3":
                    IPantalla.mensaje('usuario', 'actualizar')
                    break

                elif opcion == "4":
                    IPantalla.mensaje('aux', 'salir')
                    exit()

                else:
                    IPantalla.mensaje('aux', 'opcion_invalida')
                    IPantalla.limpiar_pantalla()

            except ValueError:
                IPantalla.mensaje('aux', 'opcion_invalida')
                IPantalla.limpiar_pantalla()

        @staticmethod
        def limpiar_pantalla():
            return system('cls')

        @staticmethod
        def mensaje(__clave, __nido, __nombre = None):
            
            yield IPantalla.__diccionario[__clave][__nido]

        
        


        
        
        
    


        
        
        
    
