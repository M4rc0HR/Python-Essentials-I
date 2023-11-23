


# Pregunta 1: ¿Qué ocurrirá al intentar ejecutar el siguiente fragmento de 
# código y por qué?


# def factorial(n):
#     return n * factorial(n - 1)
 
 
# print(factorial(4))


# Infinito ERROR


# Pregunta 2: ¿Cuál es la salida del siguiente fragmento de código?

def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)

print(fun(25))

# El OUTPUT es:
    # 25 + 28 + 3 = 56


