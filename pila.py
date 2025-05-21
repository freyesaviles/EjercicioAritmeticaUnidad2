# Clase básica para manejar una pila
class Pila:
    def __init__(self):
        self.datos = []

    def apilar(self, valor):
        self.datos.append(valor)

    def desapilar(self):
        return self.datos.pop()

    def cima(self):
        return self.datos[-1] if self.datos else None

    def vacia(self):
        return len(self.datos) == 0