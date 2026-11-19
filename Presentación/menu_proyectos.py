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

    
    def obtener_titulo(self):
        return "PROYECTOS"

    def obtener_opciones(self):
        return self._OPCIONES

    def ejecutar(self, accion):
        if accion == "crear_proyecto":
            self._crear_proyecto()
        elif accion == "asignar_proyecto":
            self._asignar_empleado()
        elif accion == "consultar_proyecto":
            self._consultar_proyecto()
        elif accion == "historial_registros":
            self._historial_registros()
        else:
            super().ejecutar(accion)

    def _crear_proyecto(self):
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
            proyecto_id = self.servicio.registrar_proyecto(self.usuario, proyecto)
            print(f"Proyecto registrado correctamente con ID {proyecto_id}.")
        except (ValueError, PermissionError, RuntimeError, ConnectionError) as error:
            print(f"Error: {error}")

    def _consultar_proyecto(self):
        try:
            proyecto = self.servicio.consultar_proyecto(
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

    def _asignar_empleado(self):
        try:
            proyecto_id = int(input("ID del proyecto: ").strip())
            empleado_id = int(input("ID del empleado: ").strip())
            self.servicio.asociar_empleado_proyecto(
                self.usuario, proyecto_id, empleado_id
            )
            print("Empleado asociado al proyecto correctamente.")
        except (ValueError, PermissionError, RuntimeError) as error:
            print(f"Error: {error}")

    def _historial_registros(self):
        try:
            proyecto_id = int(input("ID del proyecto: ").strip())
            registros = self.servicio.consultar_historial_proyecto(
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