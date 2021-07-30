import random

def run():
     numeror = random.randint(1,100)
     numeroe = int(input("Ingrese un numero del 1 al 100"))
     while numeror != numeroe:
         if numeroe < numeror:
            print("El numero es mayor")    
         if numeroe > numeror:
            print("El numero es menor")    
         numeroe = int(input("Ingrese un numero del 1 al 100"))

     print("Ganaste")



if __name__ == '__main__':
    run()