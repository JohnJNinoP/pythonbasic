import os
import random

# DATA = ['\n', ' ', ' ', ' ', ' ', ' ', ' ', '+', '-', '-', '-', '+', '\n', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', '|', '\n', ' ', ' ', ' ', ' ', ' ', ' ', 'O', ' ', ' ', ' ', '|', '\n', ' ', ' ', ' ', ' ', ' ', '/', '|', '\\', ' ', ' ', '|', '\n', ' ', ' ', ' ', ' ', ' ', '/', ' ', '\\', ' ', ' ', '|', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '\n', ' ', ' ', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=']
DATA = ['\n', ' ', ' ', ' ', ' ', ' ', ' ', '+', '-', '-', '-', '+', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '\n', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', '\n', ' ', ' ', ' ', ' ', '=', '=', '=', '=', '=', '=', '=', '=']
ERROR = [{19:"|"},{31:"O"},{42:"/"},{43:"|"},{44:"\\"},{54:"/"},{56:"\\"}]
ERRORESTOTALES = 7

def run():
    palabras = []
    conteo_error = 0
    with open('./archivos/palabras.txt','r',encoding="utf-8") as file:
        for i in file:
            palabras.append(i.replace('\n',"").upper())

    # print(palabras)
    palabra = random.choice(palabras);
    # print(palabra)
    palabra_encontrada = []
    palabra_encontrada_guion = []
    for letra in palabra:
        palabra_encontrada.append(letra)
        string = str(letra)
        if(string.strip() !=''):
            palabra_encontrada_guion.append('_')
        else:
            palabra_encontrada_guion.append(string)

    # print(palabra_encontrada)    
    # print(palabra_encontrada_guion)

    while(conteo_error<=ERRORESTOTALES):
        # os.system("cls")
        ahorca = []
        contar = 1

        for i in DATA:
            ahorca.append(i)

        for i in ERROR:
            if contar>conteo_error:
                break
            for key,value in i.items():
                ahorca[key] = value
            contar +=1

        toy = """"""
        for i in ahorca:
            toy = toy + i
        print(toy)
        print("\n")
        
        palabra_encontrada_guion_print = ""
        for letra in palabra_encontrada_guion:
            palabra_encontrada_guion_print +=letra    
        print(palabra_encontrada_guion_print)    

        no_tiene_letra = True

        

        if conteo_error<ERRORESTOTALES:
            try:
                letra = str(input("Ingrese letra: ")).upper()
                if letra in palabra_encontrada:
                    no_tiene_letra = False
                    ifor = 0
                    for i in palabra_encontrada:
                        if i==letra:
                            palabra_encontrada_guion[ifor] = letra
                        ifor += 1  

                    if palabra_encontrada_guion == palabra_encontrada:
                        print("Ganaste")
                        conteo_error = ERRORESTOTALES+1
            except ValueError:
                print("letra no valida")
        else:
            print("Perdiste")
        if no_tiene_letra:
            conteo_error +=1
        
        # print(conteo_error)

if __name__ == '__main__':
    run()