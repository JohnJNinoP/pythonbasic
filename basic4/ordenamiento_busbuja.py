
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

    conteo = []
    print(ordenamiento_burbuja(lista,conteo))
    print(len(conteo))
    
def ordenamiento_burbuja(lista,conteo):
    
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1): # O(n) * O(n) = O(n * n) = O(n**2)
            conteo.append(1)
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    

    return lista
if __name__ == '__main__':
    run()