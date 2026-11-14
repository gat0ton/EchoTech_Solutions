from Presentación.menu_area import MenuArea

class MenuProyectos(MenuArea):

    _OPCIONES = [
        
        ("Crear proyecto", "crear_proyecto"),                                
        ("Editar proyecto", "editar_proyecto"),                              
        ("Eliminar proyecto", "eliminar_proyecto"),                          
        ("Asignar empleado a proyecto", "asignar_proyecto"),                 
        ("Desasignar empleado de proyecto", "desasignar_proyecto"),          
        ("Informe de proyectos", "generar_informes"),                        
        ("Informe de registros de tiempo", "generar_informes"),              
        ("Registrar mis horas", "registrar_horas"),                          
    ]

    
    def obtenerTitulo(self):
        return "PROYECTOS"

    def obtenerOpciones(self):
        return self._OPCIONES