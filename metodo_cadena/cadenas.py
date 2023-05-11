"""      EJERCICIO DE CADENAS 
mensaje ="hola"
mensaje +=" "
mensaje +="jorge"
print(mensaje)

print("concatenar:")
mensaje1 ="holas"
mensaje2 =" "
mensaje3 ="luis"
print(mensaje1 + mensaje2 + mensaje3)

print("Buscar psosicion de una subcadena:")
mensaje1 ="hola luis"
subcadena= mensaje1.find("luis")
print(subcadena)


print("Extraer subcadena dado  2 posiscion:")
mensaje1 ="hola luis"
estraer_subcadena= mensaje1[1:7]
print(estraer_subcadena)
 
print("Comparar si es falso o verdadero:")
mensaje1 ="hola"
mensaje2 = "hol"
print(mensaje1 == mensaje2)

nombre = toto
bien =f"hola {nombre}  ?como estas?"
print("ola" in bien) #busca el ola, si esta, si es true
print("otla" not in bien) #pregunta si no esta el otla, es true, no esta
print("hola" not in bien) #pregunta si no esta el otla, es FALSE, si esta


##################

#opcion 1
print("Longitud de una cadena")
print("Hola tienes ", len("hola"), " caracteres")

#opcion 2
longitud = len("hola a todos")
print("La 'longitud' tienes ", longitud, " caracteres")

######

#opcion 1
print("\n")
nombre="jorge"
edad=20
print("Hola {} tienes {}".format(nombre,edad))

#opcion 2
nombre="jorge"
edad=22
print("Hola {0} tienes {1}".format(nombre,edad))

#opcion 3
print("Hola {nombre} tienes {edad}".format(nombre="jorge",edad=23))

#opcion 4
nombre="jorge"
edad=22
altura=1.2
print(f"Hola {nombre} tienes {edad} y de estatura {altura} metro")

#opcion 5
nombre=input("Cual es tu nombre: ")
num1=22
num3=1
print(f"Hola {nombre} el resultado de {num1} + {num3} es: {num1 + num3}")


####

#Eliminacion de caracteres y espacios, seleccionado solo de inicio y final
cadena="Hola Jorge"
print(cadena)

cadena=cadena.strip("rgHe")
print(cadena)


#Eliminacion de caracteres y espacios, seleccionado solo del final
cadena="Hola Jorge"
print(cadena)

cadena=cadena.rstrip("He")
print(cadena)


#Eliminacion de caracteres y espacios, seleccionado solo de inicio
cadena="Hola Jorge"
print(cadena)

cadena=cadena.lstrip("Hoe")
print(cadena)


#########################

cadena1 = "Hola,Maquina,Como,Estas"
cadena2 = "Bienvenido maquinola"

#convierte a mayusculas
mayusc = cadena1.upper()

#convierte a minusculas
minusc = cadena1.lower()

#primera letra en mayuscula
primer_letra_mayusc = cadena1.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_find = cadena1.find("D")

#buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepciòn
busqueda_index = cadena1.index("H")

#si es numerico, devolvemos true, sino devolvemos false
es_numerico = cadena1.isnumeric()

#si es alfanumèrico devolvemos true, sino devolvemos false
es_alfanumerico = cadena1.isalpha()

#contamos coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("la ma")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asì devuelve True
empieza_con = cadena1.startswith("H")

#verificamos si una cadena termina con otra cadena dada, si es asì devuelve True
termina_con = cadena1.endswith("H")

#si el valor 1, se encuentra en la cadena original, remplaza el valor 1 de la misma, por el valor 2
cadena_nueva = cadena1.replace(","," ")

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")

print(cadena_separada[0])

"""