import aproximacion
import busquedabinaria

def run():
    menu = """
        Ingrese un metodo para encontrar la raiz
        1.Aproximacion
        2.Busqueda binara
    """
    seleccion = int(input(menu))

    if seleccion == 1:
        a =  aproximacion.run()
    elif seleccion == 2:
        a = busquedabinaria.run()
    else:
        print('No valido')

if __name__ == '__main__':
    run()