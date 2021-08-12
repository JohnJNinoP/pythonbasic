def run():
    ordensuperior(hola)
    ordensuperior(mundo)

def hola():
    return "hola"

def mundo():
    return "mundo"

def ordensuperior(func):
    print(func())

if __name__ == '__main__':
    run()