from conversor import Conversor
from evaluador import Evaluador

# Programa principal para convertir y evaluar una expresión aritmética
if __name__ == "__main__":
    # Expresión aritmética a evaluar, puede cambiar por otra si se desea
    # Se debe usar espacios entre los números y operadores
    expresion = "5 * 4 + ( 9 / 3 + 8 * 2 )"

    conv = Conversor()
    eval = Evaluador()

    postfija = conv.a_postfijo(expresion)
    print("Postfija:", ' '.join(postfija))

    resultado = eval.evaluar(postfija)
    print("Resultado:", resultado)