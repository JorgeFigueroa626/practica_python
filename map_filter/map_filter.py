def nult(n):
    return n *5

lista=[1,2,3,4,5]
lista_map = list(map(nult,lista))
print(lista_map)

def cursos(c):
    return c.upper()

tupla=('php','python','java','html')
tupla_map =tuple(map(cursos,tupla))
print(tupla_map)

def impar(n):
    if(n % 2 == 1):
        return n

lista=[1,2,3,4,5,6,7,8,9]
tupla_map =tuple(filter(impar,lista))
print(tupla_map)