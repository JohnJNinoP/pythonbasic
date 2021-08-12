def divisor(num):
    try:
        divisor = []
        if num <= 0:
            raise ValueError("El valor debe ser mayor a cero") # lanza un error controlado
        for i in range(1,num):
            if num % i == 0:
                divisor.append(i)
        return divisor
    except ValueError as ve:
        print(ve)
        return []
    # finally:
    #     return []

def run():
    try:
        number = int(input("Input one number"))
        print(divisor(number))
    except ValueError:
        print("Debe ingresar un numero")

if __name__ == '__main__':
    run()