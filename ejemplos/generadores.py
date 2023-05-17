#generadores 2 elementos
def devuelve_ciudades(*ciudades):
    for elem in ciudades:
        yield elem

return_ciudad= devuelve_ciudades("Santa", "Beni", "La Pax", "Tarija")
print(next(return_ciudad))
print(next(return_ciudad))

#generadores de subelementos
def devuelve_ciudades(*ciudades):
    for elem in ciudades:
        #for sub  in elem:
        yield from elem
            

return_ciudad= devuelve_ciudades("Santa", "Beni", "La Pax", "Tarija")
print(next(return_ciudad))
print(next(return_ciudad))