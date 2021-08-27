# Prueba clases

class Persona : 
    def __init__(self , nombre, edad) -> None:
        self.nombre = nombre
        self.edad = edad
        self._id = 0

    def saludar(self , otra_persona):
        return f'Hola {otra_persona.nombre} me llamo {self.nombre}'

david = Persona('David',35)
luis = Persona('Luis',32)

print(david.saludar(luis))


class Coordenada():
    def __init__(self,x,y):
        self.x = x 
        self.y= y

    def distancia(self , otra_coordemada):
        x_diff = (self.x - otra_coordemada.x)
        y_diff = (self.y - otra_coordemada.y)

        return (x_diff + y_diff)**0.5
        

coordenada1 = Coordenada(3,30)
coordenada2 = Coordenada(20,2)

print(coordenada1.distancia(coordenada2))
#Valida si es instancia
print(isinstance(coordenada1,Coordenada))