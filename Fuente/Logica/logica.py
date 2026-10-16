from os import system
from sys import exit
from .autenticador import Autenticador


class Logica:

    @staticmethod
    def limpiar():
        return system('cls') 

    
    separar     = f'\n{"=" * 40}'
    
    advertencia = f'\n{"!" * 40}\n'

    _diccionario = {
                 
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

    @staticmethod
    def mensaje(self,__clave, __nido):
        
        return self._diccionario[__clave][__nido]

    def principal(self):
        while True:

            try:

                self.limpiar()
                self.mensaje('login', 'menu')
                opcion = input(self.mensaje('aux','opcion'))


                if opcion.strip() == "1":

                    __usuario = input(self.mensaje('login','usuario'))
                    __contrasena = input(self.mensaje('login','contraseña'))

                    nombre_usuario = aut._verificar_login(__usuario, __contrasena)


                    if nombre_usuario is None:

                        IPantalla.mensaje('login','contraseña_invalida')
                        IPantalla.limpiar()

                    else:

                        IPantalla.mensaje('','',nombre_usuario)

                    
                else:

                    IPantalla.mensaje('aux','salir')
                    exit()


            except ValueError:

                IPantalla.limpiar()
                IPantalla.mensaje('aux','opcion_invalida')


    def usuario(nombre: str):
        while True:

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

        

        

        
        


        
        
        
    


        
        
        
    
