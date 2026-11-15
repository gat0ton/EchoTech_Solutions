from Presentación.menu_area import MenuArea
from DTO.Administracion.proyecto_dto import ProyectoDTO

class MenuProyectos(MenuArea):

    _OPCIONES = [
        
        ("Crear proyecto", "crear_proyecto"),                                
        ("Editar proyecto", "editar_proyecto"),                              
        ("Eliminar proyecto", "eliminar_proyecto"),                          
        ("Asignar empleado a proyecto", "asignar_proyecto"),                 
        ("Desasignar empleado de proyecto", "desasignar_proyecto"),          
        ("Consultar proyecto", "consultar_proyecto"),
        ("Historial de registros", "historial_registros"),
        ("Registrar mis horas", "registrar_horas"),                          
    ]

    
    def obtenerTitulo(self):
        return "PROYECTOS"

    def obtenerOpciones(self):
        return self._OPCIONES

    def ejecutar(self, accion):
        if accion == "crear_proyecto":
            self._crearProyecto()
        elif accion == "asignar_proyecto":
            self._asignarEmpleado()
        elif accion == "consultar_proyecto":
            self._consultarProyecto()
        elif accion == "historial_registros":
            self._historialRegistros()
        else:
            super().ejecutar(accion)

    def _crearProyecto(self):
        print("\n--- CREAR PROYECTO ---")
        try:
            proyecto = ProyectoDTO(
                input("Nombre del proyecto: ").strip(),
                input("Departamento: ").strip(),
                int(input("Horas del registro: ").strip()),
                input("Fecha del registro (AAAA-MM-DD): ").strip(),
                int(input("ID asociado al registro: ").strip()),
                input("País: ").strip(),
                float(input("Presupuesto en CLP: ").strip()),
                None,
                None,
                None,
            )
            proyecto_id = self.servicio.registrarProyecto(self.usuario, proyecto)
            print(f"Proyecto registrado correctamente con ID {proyecto_id}.")
        except (ValueError, PermissionError, RuntimeError, ConnectionError) as error:
            print(f"Error: {error}")

    def _consultarProyecto(self):
        try:
            proyecto = self.servicio.consultarProyecto(
                self.usuario, int(input("ID del proyecto: ").strip())
            )
            print(f"\n--- {proyecto['nombre']} ---")
            print(f"Ubicación: {proyecto['pais']}")
            print(f"Departamento: {proyecto['departamento']}")
            print(f"Presupuesto CLP: {proyecto['presupuesto_clp']}")
            print(
                f"Presupuesto convertido: {proyecto['presupuesto_local']} "
                f"{proyecto['moneda']}"
            )
            print("Empleados asociados:")
            if not proyecto["empleados"]:
                print("  No hay empleados asociados.")
            for empleado in proyecto["empleados"]:
                print(
                    f"  - {empleado['id']}: {empleado['nombre']} "
                    f"({empleado['puesto']})"
                )
        except (ValueError, PermissionError, RuntimeError) as error:
            print(f"Error: {error}")

    def _asignarEmpleado(self):
        try:
            proyecto_id = int(input("ID del proyecto: ").strip())
            empleado_id = int(input("ID del empleado: ").strip())
            self.servicio.asociarEmpleadoProyecto(
                self.usuario, proyecto_id, empleado_id
            )
            print("Empleado asociado al proyecto correctamente.")
        except (ValueError, PermissionError, RuntimeError) as error:
            print(f"Error: {error}")

    def _historialRegistros(self):
        try:
            proyecto_id = int(input("ID del proyecto: ").strip())
            registros = self.servicio.consultarHistorialProyecto(
                self.usuario, proyecto_id
            )
            print(f"\n--- HISTORIAL DEL PROYECTO {proyecto_id} ---")
            if not registros:
                print("No hay registros para este proyecto.")
            for registro in registros:
                print(
                    f"Fecha: {registro['fecha']} | Horas: {registro['horas']} | "
                    f"ID asociado: {registro['id_asociado']}"
                )
        except (ValueError, PermissionError, RuntimeError) as error:
            print(f"Error: {error}")