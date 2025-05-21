from pila import Pila

# Evalúa una expresión en postfijo usando una pila
class Evaluador:
    def evaluar(self, tokens):
        pila = Pila()

        for token in tokens:
            if token.isdigit():
                pila.apilar(int(token))
            else:
                b = pila.desapilar()
                a = pila.desapilar()
                if token == '+':
                    pila.apilar(a + b)
                elif token == '-':
                    pila.apilar(a - b)
                elif token == '*':
                    pila.apilar(a * b)
                elif token == '/':
                    pila.apilar(a // b)
                elif token == '^':
                    pila.apilar(a ** b)

        return pila.desapilar()