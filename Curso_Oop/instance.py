
class Sumar:
    def __init__(self,numero1):
        self.numero1=numero1;
       

    def CalcularArea(self):
        area = (3.1416* ((self.numero1/2)**2))
        return area;

def run():
    area = Sumar(6);
    print(area.CalcularArea())


if __name__ == "__main__":
    run();

