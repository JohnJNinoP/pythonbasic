import time
from typing import final

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta


def Factorial_r(n):
    if n == 1:
        return 1

    return n * factorial(n-1)

def run():

# Se trata de medir el tiempo de respuesta

    n = 50000
    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(comienzo,final)

    comienzo = time.time()
    Factorial_r(n)
    final = time.time()
    print(comienzo,final)



if __name__ == '__main__':
    run()


    # Clases de complejidad algorítmica
# Existen distintos tipos de complejidad algorítmica:

# O(1) Constante: no importa la cantidad de input que reciba, siempre demorara el mismo tiempo.
# O(n) Lineal: la complejidad crecerá de forma proporcional a medida que crezca el input.
# O(log n) Logarítmica: nuestra función crecerá de forma logarítmica con respecto al input. Esto significa que en un inicio crecerá rápido, pero luego se estabilizara.
# O(n log n) Log lineal: crecerá de forma logarítmica pero junto con una constante.
# O(n²) Polinomial: crecen de forma cuadrática. No son recomendables a menos que el input de datos en pequeño.
# O(2^n) Exponencial: crecerá de forma exponencial, por lo que la carga es muy alta. Para nada recomendable en ningún caso, solo para análisis conceptual.
# O(n!) Factorial: crece de forma factorial, por lo que al igual que el exponencial su carga es muy alta, por lo que jamas utilizar algoritmos de este tipo.