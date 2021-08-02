def run():
    objetivo = int(input('Escoge un numero'))
    epsilon = 0.01
    paso  = epsilon**2
    respuesta = 0.0
    print(paso)
    print(abs(respuesta**2 - objetivo ))
    while abs(respuesta**2 -objetivo ) >= epsilon  and respuesta <= objetivo:
        respuesta += paso 

    if abs(respuesta**2 -objetivo ) >= epsilon :
        print(f'No se encontro la raiz cuadrada del objetivo')
    else:
        print(f'la raiz cuadrada es {respuesta}')


if __name__ == '__main__':
    run()