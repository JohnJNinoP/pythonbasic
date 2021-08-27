

class Lavadora:
    
    def __init__(self):
        self._tiempo = 0

    def lavar(self,temperatura = 'alto'):
        self.temperatura = temperatura
        self._llenar_tanque_de_agua()
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self):
        print(f'Llenando el tanque de agua {self.temperatura}')

    def _anadir_jabon(self):
        print('Agegando jabon')

    def _lavar(self):
        print('Lavando')

    def _centrifugar(self):
        print('centrifugando')

if __name__ == '__main__':

    lavadora = Lavadora()
    lavadora.lavar()