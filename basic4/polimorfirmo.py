
class Persona:
    def __init__(self,nombre):
        self._nombre = nombre

    def avanza(self):
        print(f"Caminando {self._nombre}")

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanza(self):
        print(f'Pedaleando {self._nombre}')

class Patinador(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanza(self):
        print(f"patinando {self._nombre}")

def run():
    persona = Persona("Arriana")
    persona.avanza()
    ciclista= Ciclista('John')
    ciclista.avanza()
    patinador = Patinador("Katherinne")
    patinador.avanza()

if __name__ == "__main__":
    run()