
from ast import Import
import math


import math
from typing import List 

def run():
    #zip permite unir dos listas y convertirlas en una lista dentro de una tupla- clave:valor.

    names = ['juana','perezito']
    ages = [22,44];
    
    listcompren = {names:ages for (names,ages) in zip(names,ages)}
    print(listcompren)


    mi_dict = {}

    for i in range(1,100):
        if i % 3 !=0:
            mi_dict[i] = i**3;
        print(mi_dict)

    mi_dict2 = {i: i**3 for i in range(1,50) if i % 3 !=0 }

    print("-------------------")
    print(mi_dict2)

    mi_dict3 = {i:math.sqrt(i) for i in range(1,1000)};
    print(mi_dict3)

if __name__ == "__main__":
    run();            