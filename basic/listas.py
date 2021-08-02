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

    
if __name__ == '__main__':
    run()