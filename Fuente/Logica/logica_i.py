class Menu:

    @staticmethod
    def _mensaje(clave, nido, nombre = None, genero = None):

        if not nombre or genero:

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
                                
                                'contraseña_invalida': "Contraseña o ID invalidos, por favor vuelve a intentarlo.",
                                
                                'bienvenida' : "Bienvenido, " + "!"},
            
            
                            'usuario' : {
            
                                'menu': f"""{separar}
                                1.- Registrar Horas
                                2.- Consultar tus Proyectos
                                3.- Actualizar tus Datos
                                4.- Salir
                                {separar}"""},
            
                            'conexion' : {
                                
                                'conexion_e' : "Conexión con Base de Datos Exitosa!",
                                
                                'conexion_f': "Conexión Fallida, intentalo mas tarde."},
            
                            'registro' :{
            
                                'opcion' : "Horas Trabajadas: "}}

            return _diccionario[clave][nido]
        
        elif genero == 'M':
                return f"Bienvenida, {nombre}"
            
        else:
            return f"Bienvenido, {nombre}"
print(Menu._mensaje('usuario', 'menu'))