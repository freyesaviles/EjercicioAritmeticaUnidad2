from pila import Pila

# Convierte una expresión infija a postfija usando una pila
class Conversor:
    def __init__(self):
        self.prioridad = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def a_postfijo(self, expresion):
        pila = Pila()
        resultado = []
        tokens = expresion.split()

        for token in tokens:
            if token.isdigit():
                resultado.append(token)
            elif token == '(':
                pila.apilar(token)
            elif token == ')':
                while pila.cima() != '(':
                    resultado.append(pila.desapilar())
                pila.desapilar()
            else:  # operador
                while (not pila.vacia() and pila.cima() != '(' and
                       self.prioridad[token] <= self.prioridad.get(pila.cima(), 0)):
                    resultado.append(pila.desapilar())
                pila.apilar(token)

        while not pila.vacia():
            resultado.append(pila.desapilar())

        return resultado