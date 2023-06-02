#creando un conjunto con set()
conjunto = set(["Dato 1"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato 1", "dato 2"])
conjunto2 = {conjunto1,"dato 3"}
print(conjunto2)

#Teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {2,4,6,8}

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

#verificar si hay algùn nùmero en comun
resultado = conjunto2.isdisjoint(conjunto1)


#print(resultado)

###----------CONJUNTO----------------
set ={1,2,3,4}

#AGREGAR
#set.add(5)

#ELIMINAR
#set.clear()

#DESCARTAR UN NUMERO
#set.discard(2)

#eliminar
#set.remove(3)
#print(set)

#-------#############

a={1,2,3,4,5}
b={4,5,6,7,8,9,0}

#union
print(a | b)

#intercentado 4,5
print(a & b)

#diferencia 123
print(a  - b)

#diferencia simetrica 1236789
print(a ^ b)