 
#Programa que adivina un numero aleatorio

import random

def run():

    naleatorio = random.randint(1,100);

    edad = int(input("Digite su edad: "));

    numero1 = int(input("digite un numero1"));

    while naleatorio != numero:
       
        if numero < naleatorio:
            print("El numero digitado es menor, digita un numero mayor");
        
        if numero > naleatorio:
            print("El numero digitado es mayor, digita un numero menor");
            
        numero = int(input("Digite un numero: "));
        
        
    print("\nGanaste: Dx");

if "__name__" == "__main__":
    run();

run()