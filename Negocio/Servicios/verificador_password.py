import hashlib
import secrets

class VerificadorPassword:
    

    _ALGORITMO = "sha256"
    _BYTES_SALT = 16  

    def generar(self, password, salt=None):
        if salt is None:
            salt = secrets.token_hex(self._BYTES_SALT)
        digest = hashlib.sha256((salt + password).encode("utf-8")).hexdigest()
        return f"{self._ALGORITMO}${salt}${digest}"

    def generarComoGuardado(self, password, hashGuardado):
        partes = hashGuardado.split("$")
        salt = partes[1] if len(partes) == 3 else ""
        return self.generar(password, salt)