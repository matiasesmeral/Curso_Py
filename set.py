
# los sets son un conjunto de datos[estructura de datos] el cual guarda datos no repetidos.
# los conjuntos se definen asi: name = {'dato1',2,true}

phrases = "hola"
sets1 = set(phrases);

set2 = {'1','2','4','2'}

print(set2)
print(sets1)
print('h' in sets1 )

#add
sets1.add('s')
print(sets1)

#uptdate
sets1.update('f','g')
print(sets1)

#delete
set2.remove('1')
print(set2)

#clear
set2.clear()
print(len(set2))

#------------------------------------------------

#operations whith sets
set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

set_c = set_a.union(set_b)

print(set_c)

print(set_a | set_b)

print(set_a & set_b)

print(set_a.difference(set_b) )

print(set_a.symmetric_difference(set_b))






