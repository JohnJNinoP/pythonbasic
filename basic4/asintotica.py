# ley de la suma
# Validar el peor de los casos 
def ff(n):
    for i in range(n):
        print(i)
    
    for i in range(n):
        print(i)
# o(n) + o(n) = o(n+n) = o(2n) = o(n)

# ley de la suma
def fff(n):
    for i in range(n):
        print(i)
    
    for i in range(n * n):
        print(i)
# o(n) + o(n * n) = o(n + n^2) = o(n^2)

# ley de la multiplicacion
def ffff(n):
    for i in range(n):
          for j in range(n):
            print(i,j)  
# o(n) * o( n) = o(n + n) = o(n^2)

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)
# o(2**n)
n = 5

print(ff(n))
print(fff(n))
print(ffff(n))
print(fibonacci(n))

# Clases de complejidad algorítmica
# Existen distintos tipos de complejidad algorítmica:

# O(1) Constante: no importa la cantidad de input que reciba, siempre demorara el mismo tiempo.
# O(n) Lineal: la complejidad crecerá de forma proporcional a medida que crezca el input.
# O(log n) Logarítmica: nuestra función crecerá de forma logarítmica con respecto al input. Esto significa que en un inicio crecerá rápido, pero luego se estabilizara.
# O(n log n) Log lineal: crecerá de forma logarítmica pero junto con una constante.
# O(n²) Polinomial: crecen de forma cuadrática. No son recomendables a menos que el input de datos en pequeño.
# O(2^n) Exponencial: crecerá de forma exponencial, por lo que la carga es muy alta. Para nada recomendable en ningún caso, solo para análisis conceptual.
# O(n!) Factorial: crece de forma factorial, por lo que al igual que el exponencial su carga es muy alta, por lo que jamas utilizar algoritmos de este tipo.