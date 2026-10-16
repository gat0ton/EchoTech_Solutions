from Fuente.Logica import Flujo

nombre = Flujo.principal(True)
if nombre is not None:
    Flujo.usuario(True, nombre)
