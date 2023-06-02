print(list(range(0,9)))


#LISTA EN VERTICAL
# for i in range(0,9):
#     print(i, end=' - ')

#RECORE EN 2 
# for i in range(2,10,2):
#     print(i, end=' - ')

#FORMA DE TRIANGULO
  #el numero final
for num in range(10):
    #el numero inicial
    for i in range(num):
        print(i, end=' ')
    print()

#revertir una lista  
for i in reversed(range(0,9)):
    print(i)
    
#generar lista
genera =list(range(0,9))
print("Lista ", genera)

#################################

#crear una lista apartir de otra

curso =[letras for letras in 'python']
print(curso)

#crear una lista apartir de otra(SI KIERE MULTIPLICA POR 2)
lista_a=[1,2,3,4,5,6]
lista_b=[]

for i in lista_a:
    para_lista_b=i # *2
    lista_b.append(para_lista_b)
print("lista b ",lista_b)
###
lista_b=[i*2 for i in lista_a]
print(lista_b)