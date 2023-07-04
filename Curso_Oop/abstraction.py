
class Lavadora:

    def __init__(self):
        pass;

    def lavar(self, temperatura='caliente'):
        self ._llenar_estanque_agua(temperatura);
        self ._anadir_jabon()
        self ._lavar()
        self ._centrifugar()
    
    def _llenar_estanque_agua(self,temperatura):
        print(f'llenando el estanque de agua a una temperatura {temperatura}');

    def _anadir_jabon(self):
        print('anadiendo jabon.');

    def _lavar(self):
        print('lavando.')    

    def _centrifugar(self):
        print('centrifugando la ropa');

def run():
        lavadora = Lavadora();
        lavadora.lavar()

if __name__==  '__main__':
    run();