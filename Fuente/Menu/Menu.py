from os import system

class Menu:

    @staticmethod
    def mensaje(clave, nido):

        separar = str("=" * 40)
        

        diccionario = {
            'aux': 
            {
                'opcion' : "Ingrese una Opcion: ",
                'invalido': "Opción Invalida, por favor vuelve a Intentarlo.",                
                'salir': "Saliendo del programa..."
            },
            'login': 
            {
                'menu': f"{separar}\nBienvenido al menú principal\n1. Iniciar Sesión\n2. Salir\n{separar}\n",
                'id': "Ingresa tu ID de empleado",
                'contraseña': "Ingresa tu contraseña: ",
                'contraseña_invalida': "Contraseña o ID invalidos, por favor vuelve a intentarlo."
            },
            'usuario': 
            {
                'menu': f"{separar}\n
                1.- Registrar Horas\n2.- Consultar tus Proyectos\n3.- Actualizar tus Datos\n4.- Salir\n{separar}"
            },
        }

        return diccionario[clave][nido]
    @staticmethod
    def limpiar_pantalla():
        return system('cls')