def prioridad(op):
    if op == '^':
        return 3
    elif op in ('*', '/'):
        return 2
    elif op in ('+', '-'):
        return 1
    else:
        return 0

def infija_a_postfija(expresion):
    pila = []
    postfija = []
    tokens = expresion.split()

    for token in tokens:
        if token.isdigit():
            postfija.append(token)
        elif token == '(':
            pila.append(token)
        elif token == ')':
            while pila and pila[-1] != '(':
                postfija.append(pila.pop())
            pila.pop()  # Eliminar '('
        else:  # operador
            while pila and prioridad(pila[-1]) >= prioridad(token):
                postfija.append(pila.pop())
            pila.append(token)

    while pila:
        postfija.append(pila.pop())

    return postfija

def evaluar_postfija(postfija):
    pila = []

    for token in postfija:
        if token.isdigit():
            pila.append(int(token))
        else:
            b = pila.pop()
            a = pila.pop()
            if token == '+':
                pila.append(a + b)
            elif token == '-':
                pila.append(a - b)
            elif token == '*':
                pila.append(a * b)
            elif token == '/':
                pila.append(a // b)
            elif token == '^':
                pila.append(a ** b)

    return pila[0]

# Para evaluar cada expresion, cambie los valores en la variable expresion
expresion = "6 + 4 * ( 9 + 5 * 2 - 3 )"
postfija = infija_a_postfija(expresion)
print("Postfija:", ' '.join(postfija))
print("Resultado:", evaluar_postfija(postfija))