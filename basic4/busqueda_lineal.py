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
            lista = [random.randint(0,tamano_lista) for i in range(tamano_lista)]
            stop = True
            
        except ValueError:
            print("No es un numero")

    
    print(busqueda_lineal(lista,objetivo))

    
def busqueda_lineal(lista,objetivo):
    match = False
    conteo = 0
    for i in lista:
        conteo += 1
        if i == objetivo:
            match = True
            break
    print(conteo)
    return match

if __name__ == '__main__':
    run()