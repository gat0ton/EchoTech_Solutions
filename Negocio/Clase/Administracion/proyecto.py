from Negocio.Clase.Administracion.registro import Registro


class Proyecto:
    def __init__(
        self,
        nombre: str,
        departamento: str,
        registro: Registro,
        pais: str,
        presupuesto_clp: float,
        moneda: str,
        presupuesto_local: float,
        tasa_conversion: float,
    ):
        if not nombre or not pais:
            raise ValueError("El proyecto y el país son obligatorios.")
        if not isinstance(presupuesto_clp, (int, float)) or isinstance(
            presupuesto_clp, bool
        ) or presupuesto_clp <= 0:
            raise ValueError("El presupuesto en CLP debe ser mayor que 0.")
        if presupuesto_local <= 0 or tasa_conversion <= 0:
            raise ValueError("La conversión del presupuesto debe ser mayor que 0.")
        if not departamento or registro is None:
            raise ValueError("El proyecto debe asociarse a un departamento y un registro.")

        self.nombre = nombre.strip()
        self.departamento = departamento
        self.registro = registro
        self.pais = pais.strip()
        self.presupuesto_clp = presupuesto_clp
        self.moneda = moneda.upper()
        self.presupuesto_local = presupuesto_local
        self.tasa_conversion = tasa_conversion
