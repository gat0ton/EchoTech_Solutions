from subprocess import run
import time


class Utilidades:

    @staticmethod
    def separar():
        return f'{"=" * 40}'

    @staticmethod
    def advertencia():
        return f'{"!" * 40}'

    @staticmethod
    def _limpiar():
        return run('cls', shell= True)

    @staticmethod
    def salir():
        ciclos = 0.0
        cadena = ""
        mensaje = "Saliendo del Programa..."
        while (ciclos / len(mensaje)) != 3:
            if (ciclos / len(mensaje)) > 0:
                cadena = ""
            for i in mensaje:
                cadena= cadena + i
                print(cadena)
                time.sleep(.016)
                run('cls',shell=True)
                ciclos+= 1


class Mensaje:

    @staticmethod
    def _mostrar(clave=None, nido=None, nombre=None, genero=None):
        __diccionario = {
            'aux': {
                'opcion'          : "Ingrese una Opcion: ",
                
                'valor'           : "Ingrese un Valor: ",
                
                'invalido'        : "Opción Invalida, por favor vuelve a Intentarlo.",
                
                'salir'           : "Saliendo del programa...",
                
                'opcion_invalida' : Utilidades.advertencia() +
                                    """Opción no válida, por favor intente de nuevo.
                                    """  + Utilidades.advertencia()},

            'login': {
                'menu': f"¡¡Bienvenido al menú principal!!\n\n{Utilidades.separar()}\n1. Iniciar Sesión\n2. Salir\n{Utilidades.separar()}\n",

                'id': "Ingresa tu ID de empleado: ",
                
                'usuario': "Ingresa tu ID de empleado: ",
                
                'contraseña': "Ingresa tu contraseña: ",
                
                'contraseña_invalida': "Contraseña o ID invalidos, por favor vuelve a intentarlo."},


            'usuario' :{

                'menu': f"""{Utilidades.separar()}
                1.- Registrar Horas
                2.- Consultar tus Proyectos
                3.- Actualizar tus Datos
                4.- Salir
                {Utilidades.separar()}"""},

            'conexion' : {
                
                'conexion_e' : "Conexión con Base de Datos Exitosa!",
                
                'conexion_f': "Conexión Fallida, intentalo mas tarde."},

            'registro' :{

                'opcion' : "Horas Trabajadas: "}}
        if nombre and genero == 'F':
                return f"Bienvenida, {nombre}"
        elif  nombre and genero == 'H':
            return f"Bienvenida, {nombre}"
        else:
            return __diccionario[clave][nido]