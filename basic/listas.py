def run():
    lista = [1 ,2,3,4,5,6]
    print(lista)
    lista.append(False)  # agregar elemento
    print(lista)
    print(lista[0])      # un elemento de la lista
    print(lista.pop(1))  # Borrar elemento
    print(lista)
    print(lista[1::])
    print(lista + [1])   # Suma de listas
    print(lista * 2)     # multiplica lista


    # se asigna la misma direccion en memeria
    a = [1,2,3]
    b = a
    # se clona y crea una nueva direccion de memoria
    c= list(a)
    d = a[::]

    # list de filtro de lista en una linea
    my_list = list(range(0,100))
    doblar = [i*2 for i in my_list ]
    print(doblar)
    pares  = [i for i in my_list if i % 2 == 0]
    print(pares)
    
if __name__ == '__main__':
    run()