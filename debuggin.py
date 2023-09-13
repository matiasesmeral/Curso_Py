#programa que permite saber si un numero es primo o no, aplicando funciones.


def numPrimo(x):
    
    if x % 2 == 0:
        return True
    else:
        return False;    

def run():
    
    try:
        num = input("Digite un numero: ")
        
        if int(num) < 0:
            raise TypeError ("Error digite numeros positivos");
        print(numPrimo(4))
    
    except ValueError:
        print("Debe digitar solo numeros no letras");

    #assert num.isnumeric(),"Error debe ingresar un numero"
    #assert num.isnumeric() and int(num) < 1 ,"Error debe ingresar un numero mayor a 1"
    
    

if __name__ == "__main__":
    run();    