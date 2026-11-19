class Usuario:

    _PERMISOS = {
        "Administrador": {
            "registrar_usuario",
            "registrar_empleado",
            "modificar_mis_datos",
            "modificar_salario",
            "crear_departamento",
            "editar_departamento",
            "buscar_departamento",
            "eliminar_departamento",
            "asignar_departamento",
            "asignar_gerente",
            
            "crear_proyecto",
            "editar_proyecto",
            "eliminar_proyecto",
            "asignar_proyecto",
            "desasignar_proyecto",
            
            "generar_informes",
            "consultar_proyecto",
            "historial_registros",
        },
        "Empleado": {
            "ver_perfil",
            "ver_contacto",
            "ver_ficha",
            "registrar_horas",
            "modificar_mis_datos",
        },
    }

    def __init__(self, username, password, rol):
        self._username = username
        self._password = password
        self._rol = rol
        self._sesionActiva = False

    def autenticar(self, username, password):
        self._sesionActiva = self._username == username and self._password == password
        return self._sesionActiva

     
    def cambiar_password(self, claveActual, claveNueva):
        if not self._sesionActiva or self._password != claveActual:
            return False
        self._password = claveNueva
        return True

    def verificar_autorizacion(self, moduloOAccion):
        return self._sesionActiva and moduloOAccion in self._PERMISOS.get(self._rol, set())

    def cerrar_sesion(self):
        self._sesionActiva = False

    def obtener_identidad(self):
        return self._username

    def actualizar_identidad(self, username):
        self._username = username

    def obtener_rol(self):
        return self._rol

    
    def tiene_rol_valido(self):
        return self._rol in self._PERMISOS