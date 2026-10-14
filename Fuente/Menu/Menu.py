from os import system

class Menu:
    @staticmethod
    def limpiar_pantalla():
        return system('cls')

    @staticmethod
    def mensaje(clave, nido,nombre = None):

        separar = str("=" * 40)        
        if clave == 'login' and nido == 'bienvenida':
                return f"Bienvenido, {nombre}!"
        

        diccionario = {
            'aux': 
            {
                'opcion'  : "Ingrese una Opcion: ",
                'valor'   : "Ingrese un Valor: ",   
                'invalido': "Opción Invalida, por favor vuelve a Intentarlo.",                
                'salir'   : "Saliendo del programa...",
                'opcion_invalida': "Opción no válida, por favor intente de nuevo."
            },
            'login': 
            {
                'menu': f"{separar}\nBienvenido al menú principal\n1. Iniciar Sesión\n2. Salir\n{separar}\n",
                'id': "Ingresa tu ID de empleado: ",
                'usuario': "Ingresa tu ID de empleado: ",
                'contraseña': "Ingresa tu contraseña: ",
                'contraseña_invalida': "Contraseña o ID invalidos, por favor vuelve a intentarlo."
            },
            'usuario': 
            {
                'menu': f"{separar}\n1.- Registrar Horas" +
                "\n2.- Consultar tus Proyectos" +
                "\n3.- Actualizar tus Datos" +
                "\n4.- Salir" +
                f"\n{separar}\n",
                'proyectos': "Consultar tus Proyectos",
                'actualizar': "Actualizar tus Datos"
            },
            'conexion':
            {
            'conexion_e': "Conexión con Base de Datos Exitosa!",
            'conexion_f': "Conexión Fallida, intentalo mas tarde."
            }
        }
        indice = diccionario[clave][nido]
        

        return indice

    @staticmethod
    def mostrar_mensaje(clave, nido, nombre=None):
        print(Menu.mensaje(clave, nido, nombre))

    
