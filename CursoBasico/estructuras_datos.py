

# 1. listas , tuplas , diccionarios. 

# 1. las listas son basicamente un array en donde podemos tener multiples tipos de datos.
# se definen de la siguiente manera. lista = ["dato1",dato2...].

# 2. Las tuplas a diferencia de las listas no son modificables, es decir, tienen un tamaño fijo.
# se declaran de la siguiente manera:  tuplas = (2,3,4,5,...).

# 3. Los diccionarios, son basicamente un json en python que permite tener multiples tipos de datos.
# cabe resaltar que para acceder a ellos, se necesita de metodos especificos los cuales son:
# diccionario.value() , dicc.keys() , dicc.items(). 
# se definen de la siguiente forma: dicc = {"nombre"="juan",...}.

lis1 = ["lista1","lista2","lista3","lista4","lista5","lista6"];
lis2 = lis1[::-1];

print(lis2);
print("--------------------")
lis3 = lis2[2:3];
print(lis3);
print("--------------------")
lista1 = ["water",1,2,4];
lista1.insert(3,3);
print(lista1)
print("--------------------")
lista1.append(5)
print(lista1)
print("--------------------")
lista1.pop(0)
print(lista1)
print("--------------------")
lista1.extend(lis1);
print(lista1)
print("--------------------")
tupl3 = ("Courses",6,7,8);
lista1.extend(tupl3)
print(lista1);
print("--------------------")
for x in lista1:
    print(x)
print("--------------------")
listnew = [x for x in lis1 if "l" in x];
print(listnew)



