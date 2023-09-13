

# insertar - eliminar si el numero es 1 - agregar una lista si hay x primo - palindromo 

def addelement(lis):
    lis2 = [7,8,9]
    for x in lis:
        if x % 2 ==0:
            return lis + lis2
    print("Funcion add ejecutada-");    
    
def run():
    lis = [1,2,3,4,5]
    lis2 = [{"age":18}]
    lis3 = { "natural_nums": [1,2,3,4,5],
        "integer_nums": [-2,-1,0,1,2],
        "floats_nums" : [1.2,1.3,1.4] }
    #imprimiendo la lista
    
    for i in lis2:
        print(i," : ")

    for i,y in lis3.items():
        print(i,": ",y)    

   # for i in lis:
   #    if i % 5==0:
   #       lis.append(6)
    for i in lis:
        if i == 1:
            lis.pop();
        else:
            print(i)    

    lis3 = addelement(lis)
    print(lis3)

    x  = lambda x: x==x[::-1]
    print(x("lol"))
    
if __name__ == "__main__":
    run();