
import random


def run():
    stop = False
    tamano_lista = 0
    lista = []
    objetivo = 0
    while stop == False:
        try:
            tamano_lista = int(input("Tamaño de la lista"))
            objetivo = int(input("Numero a buscar"))
            lista = sorted([random.randint(0,100) for i in range(tamano_lista)])
            print(lista)
            stop = True
        except ValueError:
            print("No es un numero")

    conteo = []
    print(busqueda_binaria(lista,0,100, objetivo,conteo))
    print(len(conteo))
    
def busqueda_binaria(lista,inicio,final,objetivo,conteo):

    conteo.append(1)
    if inicio > final:
        return False
    
    medio = (inicio + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio]< objetivo:
        return busqueda_binaria(lista,medio+1,final,objetivo,conteo)
    else :
        return busqueda_binaria(lista,inicio,medio-1,objetivo,conteo)
    

    

if __name__ == '__main__':
    run()