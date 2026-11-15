import requests


class API:
    def __init__(self):
        self.url = "https://api.exchangerate-api.com/v4/latest/CLP"

    def convertir_clp(self, monto_clp: float, moneda_destino: str) -> dict:
        #todo: VALIDAR DATOS ANTES DE CONSULTAR LA API 
        if isinstance(monto_clp, bool) or not isinstance(monto_clp, (int, float)) or monto_clp <= 0:
            raise ValueError("El presupuesto en CLP debe ser un número mayor a 0.")

        if not isinstance(moneda_destino, str):
            raise ValueError("La moneda destino debe ser texto.")

        moneda_destino = moneda_destino.upper().strip()
        if len(moneda_destino) != 3 or not moneda_destino.isalpha():
            raise ValueError(f"Código de moneda inválido ('{moneda_destino}'). Usa 3 letras (ej: MXN).")

        try:
            #todo: TIEMPO MÁXIMO DE ESPERA (timeout)
            respuesta = requests.get(self.url, timeout=5)

            #todo: VERIFICAR CÓDIGO DE ESTADO HTTP (ej. 200 OK vs 404/500)
            respuesta.raise_for_status()

            datos = respuesta.json()

            #todo: COMPROBAR QUE LOS CAMPOS ESPERADOS ESTÉN PRESENTES
            if not isinstance(datos, dict) or "rates" not in datos or not isinstance(datos["rates"], dict):
                raise KeyError("La respuesta de la API no trajo el campo esperado 'rates'.")

            tasas = datos["rates"]

            if moneda_destino not in tasas:
                raise ValueError(f"La moneda '{moneda_destino}' no existe en la API.")

            tasa_conversion = tasas[moneda_destino]
            monto_final = round(monto_clp * tasa_conversion, 2)

            #todo: GUARDAR / RETORNAR SOLO LOS DATOS NECESARIOS (descartamos las otras 160 monedas)
            return {
                "monto_clp": monto_clp,
                "moneda_destino": moneda_destino,
                "tasa": tasa_conversion,
                "monto_convertido": monto_final
            }

        #todo: RESPUESTA CONTROLADA ANTE ERRORES
        except requests.exceptions.Timeout:
            raise ConnectionError("Tiempo de espera agotado (5s) al conectar con la API.")
        except requests.exceptions.HTTPError as e:
            raise ConnectionError(f"Error HTTP {e.response.status_code} al consultar la API.")
        except requests.exceptions.JSONDecodeError:
            raise ValueError("La API devolvió una respuesta que no es JSON válido.")
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Error de red al conectar con la API: {e}")