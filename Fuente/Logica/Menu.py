from os import system

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
                                        """  +
                                        advertencia
                    },
    
    
                'login': {
                    'menu': separar +
                    
                    "Bienvenido al menú principal\n1. Iniciar Sesión\n2. Salir\n{separar}\n",
    
                    'id': "Ingresa tu ID de empleado: ",
                    
                    'usuario': "Ingresa tu ID de empleado: ",
                    
                    'contraseña': "Ingresa tu contraseña: ",
                    
                    'contraseña_invalida': "Contraseña o ID invalidos, por favor vuelve a intentarlo."
                    },
    
    
                'usuario' : {
                    'menu': separar + 
                    "1.- Registrar Horas"  +
    
                    "\n2.- Consultar tus Proyectos" +
    
                    "\n3.- Actualizar tus Datos" +
    
                    "\n4.- Salir" +
                    separar,
    
                    'proyectos': "Consultar tus Proyectos",
                    
                    'actualizar': "Actualizar tus Datos"
                    },
    
    
                'conexion' : {
                    
                    'conexion_e' : "Conexión con Base de Datos Exitosa!",
                    
                    'conexion_f': "Conexión Fallida, intentalo mas tarde."
                    },
    
    
                'registro' :{
                    'opcion' : "Horas Trabajadas: "
    
                    }}
    

    @staticmethod
    def limpiar_pantalla():
        return system('cls')

    @staticmethod
    def mensaje(__clave, __nido, __nombre = None):
        
        yield IPantalla.__diccionario[__clave][__nido]

        
        
IPantalla.mensaje('login')

        
        
        
    


        
        
        
    
