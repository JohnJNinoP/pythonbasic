def run():
    numero = int(input("Escriba un numero"))
    if Es_Primo(numero):
        print("Es primo")
    else:
        print("No es primo")

def  Es_Primo(numero):
    contador  = 0
    for item in range(1,numero + 1):
        if item == 1 or item == numero:
            continue
        if numero % item == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False
    

if __name__ == "__main__":
    run()
