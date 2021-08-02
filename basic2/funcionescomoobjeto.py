from typing import runtime_checkable


def run():
    operacion(multiplicar,[1,2,3,4,5,6])
    operacion(sumar,[1,2,3,4,5,6])
    aplicar_operaciones(-4)

def multiplicar(n):
    return n*2

def sumar(n):
    return n+2

def operacion(f,numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado) 
    print(resultados)

def aplicar_operaciones(n):
    operaciones = [abs,float,str]

    resultado= []
    for operacion in operaciones:
        resultado.append(operacion(n))
    
    print(resultado)

if __name__ == '__main__':
    run()