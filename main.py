from Fuente.Logica import Pantalla

nombre = Pantalla.principal(True)
if nombre is not None:
    Pantalla.usuario(True, nombre)
