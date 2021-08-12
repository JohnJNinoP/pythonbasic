

def run():

    valor = 1
    for item in range(30):
        valor = valor*2
    
    print(valor)

    for item in range(1000):
        print(item) 

    menu = """Escribe
    tu 
    nombre
    """
    cadena  = input(menu)
    for  letter in cadena:
        print(letter)




if __name__ == '__main__':
    run()
    