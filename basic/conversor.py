    # pesos = input("Cuantos tienes?:")
# pesos = float(pesos);
# valorDolar = 3875
# dolaresTexto = str(round(pesos / valorDolar,2));
# print(dolaresTexto)

def CalcularValor(valor,pesos):
    return str(round(pesos / valor,2))

menu = """
Welcome to converter money

1 - CO
2 - AR
3 - MX
"""

opcion = input(menu)
pesos = input("Cuanto tienes?:")
pesos = float(pesos);

if(opcion == "1"):
    valorDolar = 3875    
elif opcion =="2":
   valorDolar = 65
else:
    valorDolar = 24

print(CalcularValor(valorDolar,pesos))