class Automovil:
    def __init__(self,modelo,marca,color) -> None:
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = "en_reposo"
        self.motor = Motor(4)

    def acelerar(self, tipo = "despacio"):
        if tipo == "rapida":
            self.motor.inyecta_gasolina(10)
        else:    
            self.motor.inyecta_gasolina(3)

        self._estado = "en_movimiento"

class Motor:
    def __init__(self,cilindro , tipo = "gasolina"):
        self.cilindros = cilindro
        self.tipo = tipo
        self._temperatura = 0
        self.velocidad = 0
        self.gasolina = 0

    def inyecta_gasolina(self, gasolina):
        self.gasolina -= gasolina

