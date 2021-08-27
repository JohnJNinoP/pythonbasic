from typing import overload

class Rectangulo:
    def __init__(self,base , altura):
        self._base = base
        self._altura = altura
    
    def area(self):
        return (self._base * self._altura)

class Cuadrado(Rectangulo):
    def __init__(self, base, altura):
        super().__init__(base, altura)    

rectangulo = Rectangulo(2,2)
cuadradro = Cuadrado(2,2)

print(rectangulo.area())
print(cuadradro.area())