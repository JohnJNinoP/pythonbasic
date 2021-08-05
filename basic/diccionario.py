def run():
    diccionario = {
        'key1' : 1,
        'key2' : 2,
        'key3' : 3
    }
    print(diccionario)
    print(diccionario['key1'])
    print(diccionario['key2'])
    print(diccionario['key3'])
    print(diccionario.__contains__('key4'))

    for pais in diccionario.keys():
        print(pais)

    for paisvalue in diccionario.values():
        print(paisvalue)

    for item in diccionario.items():
        print(item)        

    for key,value in diccionario.items():
        print(key)        
        print(value)

    # si la llave se encuentra
    validar = 'key1' in diccionario
    print(validar)     
    print('key?' in diccionario)

    # Elimiar la llave
    del diccionario['key1']

if __name__ == '__main__':
    run()