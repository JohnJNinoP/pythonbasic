
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
    print(ordenamiento_por_mezcla(lista,conteo))
    print(len(conteo))
    

def ordenamiento_por_mezcla(lista,conteo):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        # print(izquierda, '*' * 5, derecha)
        conteo.append(1)
        # llamada recursiva en cada mitad
        ordenamiento_por_mezcla(izquierda,conteo)
        ordenamiento_por_mezcla(derecha,conteo)

        # Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        # Iterador para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k +=1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        
        # print(f'izquierda {izquierda}, derecha {derecha}')
        # print(lista)
        # print('-' * 50)

    return lista


if __name__ == '__main__':
    run()