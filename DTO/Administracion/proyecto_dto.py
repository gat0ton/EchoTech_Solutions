class ProyectoDTO:
    def __init__(
        self,
        nombre,
        departamento_nombre,
        registro_horas,
        registro_fecha,
        registro_id_asociado,
        pais,
        presupuesto_clp,
        moneda,
        presupuesto_local,
        tasa_conversion,
    ):
        self.nombre = nombre
        self.departamento_nombre = departamento_nombre
        self.registro_horas = registro_horas
        self.registro_fecha = registro_fecha
        self.registro_id_asociado = registro_id_asociado
        self.pais = pais
        self.presupuesto_clp = presupuesto_clp
        self.moneda = moneda
        self.presupuesto_local = presupuesto_local
        self.tasa_conversion = tasa_conversion
