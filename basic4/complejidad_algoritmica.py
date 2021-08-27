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