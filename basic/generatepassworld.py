import random

def run():
    passworld = generatePass()
    print('Your new password is ' + passworld )

def generatePass():
    mayusculas = ['A','B','C','D','F']
    minusculas = ['a','b','c','d','f']
    simbolos = ['!','#','$','/','(',')']
    numeros = ['1','2','3','4','5','6','7','8','9','0']
    caracteres = mayusculas + minusculas + simbolos + numeros;

    contrasena = []

    for i in range(15):
        caracterramdon = random.choice(caracteres);
        contrasena.append(caracterramdon)

    contrasena = "".join(contrasena)
    return contrasena

if __name__ == '__main__':
    run()