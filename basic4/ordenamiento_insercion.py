
import random


def run():
    stop = False
    tamano_lista = 0
    lista = []
    while stop == False:
        try:
            tamano_lista = int(input("Tamaño de la lista"))
            lista = [random.randint(0,100) for i in range(tamano_lista)]
            print(lista)
            stop = True
        except ValueError:
            print("No es un numero")

    print(ordenamiento_por_insercion(lista))
    

def ordenamiento_por_insercion(lista):
    conteo = 0    
    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1
            conteo +=1
        lista[posicion_actual] = valor_actual

    print(conteo)
    return lista
if __name__ == '__main__':
    run()