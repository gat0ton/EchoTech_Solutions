import requests

class API:
    def transformador(self,):
        #? Ingresa el monto de la moneda a la que se desea convertir
        moneda = input("Ingrese la moneda a la que desea convertir (por ejemplo, EUR, GBP, JPY): ").upper()
        monto = float(input("Ingrese el monto en CLP que desea convertir: "))
        url = 'https://api.exchangerate-api.com/v4/latest/CLP'


        respuesta = requests.get(url)

        #convergencia de la monena CLP a la moneda ingresada por el usuario
        for i in respuesta.json()['rates']:
            if i == moneda:
                print(f"{monto} CLP equivale a {monto * respuesta.json()['rates'][i]} {moneda}")
                break