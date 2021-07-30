def CalcularValor(valor,pesos):
    return round(valor / pesos)


def Palindromo(name):
    name = name.lower().strip().replace(" ","")
    nameI = name[::-1]
    if name == nameI:
        return True
    else:
        return False

if __name__ == '__main__':
    name = input("Ingresa frase")
    print(Palindromo(name))


