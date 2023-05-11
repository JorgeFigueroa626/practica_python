
"""
#######################

EJERCICIO DE ENTRADAS DATOS DESDE LA CONSOLA

print("Entrada de Datos desde la Consola")
palabra = input("introduce una palabra: ")
num_int = int(input("introduce un numero: "))
num_float = float(input("introduce un numero float: "))
num_compless = complex(input("introduce un numero complejo: "))
print("String: ", palabra)
print("Entero: ", num_int)
print("Float: ", num_float)
print("Numero_complejo: ", num_compless)

nombre = input("¿Cual es tu nombre? ")
print("Hola " + nombre + " vamos realizar una operacion.")
numero1 = int(input("introduce un numero: "))
numero2 = int(input("introduce otro numero: "))
resultado = numero1 + numero2
print(nombre + " el resultado de la suma es: ", resultado)

#######################

nombre = input("¿Cual es tu nombre? ")
print("Hola " + nombre + " vamos COMPROBAR SI APROBASTE.")
numero1 = int(input("introduce tu nota de matematica: "))
numero2 = int(input(nombre + " introduce tu nota de biologia: "))
numero3 = int(input("introduce tu nota de literatura: "))
resultado = (numero1 + numero2 + numero3)/3
resultado = int(resultado)
if resultado >= 8: 
        print('"APROBASTE" ' + nombre + " TU PROMEDIO ES: ", resultado)
print("Fin.")

#######################

nombre = input("¿Cual es tu nombre? ")
print("Hola " + nombre + " vamos COMPROBAR SI APROBASTE.")
numero1 = float(input("introduce tu nota de matematica: "))
numero2 = float(input(nombre + " introduce tu nota de biologia: "))
numero3 = float(input("introduce tu nota de literatura: "))
resultado = (numero1 + numero2 + numero3)/3

if resultado >= 8:
        print('"Aprobaste" ' + nombre + " TU PROMEDIO ES: ", resultado)
        print('"Aprobaste" ' + nombre + " TU PROMEDIO ES: ", round(resultado,2))
else: 
        print('"Reprobaste" ' + nombre + " TU PROMEDIO ES: ", resultado)
        print('"Reprobaste" ' + nombre + " TU PROMEDIO ES: ", round(resultado,2))
print("Fin.")

#######################

print("****************")
print("Multiples condicionales")
print("****************")
numero=int(input("¿Saber si existe el numero?: "))
if numero == 1:
    print("El numero es 'Uno'")
elif numero == 2:
    print("El numero es 'Dos'")
elif numero == 3:
    print("El numero es 'Tres'")
elif numero == 4:
    print("El numero es 'Cuatro'")
elif numero == 5:
    print("El numero es 'Cinco'")
else:
    print("El numero solo exite haste el 5")

print("fin.")

#######################

print("****************")
print("Opciones a condicionales")
print("****************\n")

print("Menu de obciones\n")
print("opcion 1 convertir de numero a palabra")
print("opcion 2 convertir de palabra a numero \n")

opcion=int(input("¿Eliga la opcion?: "))

if opcion == 1:
    print("\n Convertir el numero a palabra. \n")

    opcion_uno=int(input("¿Eliga el numero a palabra?: "))

    if opcion_uno == 1:
        print("El numero es 'Uno'")
    elif opcion_uno == 2:
        print("El numero es 'Dos'")
    elif opcion_uno == 3:
        print("El numero es 'tres'")
    elif opcion_uno == 4:
        print("El numero es 'cuatro'")
    elif opcion_uno == 5:
        print("El numero es 'cinco'")
    else:
        print("Opcio de numero no disponible")

elif opcion == 2:
    print("\n Convertir de palabra numero. \n")

    opcion_dos=input("¿Eliga el numero a palabra?: ")
    opcion_dos= opcion_dos.lower()

    if opcion_dos == "uno":
        print("El numero es '1'")
    elif opcion_dos == "dos":
        print("El numero es '2'")
    elif opcion_dos == "tres":
        print("El numero es '3'")
    elif opcion_dos == "cuatro":
        print("El numero es '4'")
    elif opcion_dos == "cinco":
        print("El numero es '5'")
    else:
        print("Opcio de letra no disponible")

else:
    print("Opcio no disponible")

print("fin.")

#######################

print("****************")
print("Introduce dos numero a comparar")
print("****************\n")

opcion_uno=int(input("Introduce primer numero: "))
opcion_dos=int(input("Introduce segundo numero: "))

print("\n Los numero a comparar son: ", opcion_uno, " y ", opcion_dos, "\n")

if opcion_uno == opcion_dos:
    print("Es igual...")
if opcion_uno != opcion_dos:
        print("Es diferente")
if opcion_uno < opcion_dos:
        print("Es menor")
if opcion_uno > opcion_dos:
        print("Es mayor")
if opcion_uno <= opcion_dos:
        print("Es menor o igual")
if opcion_uno >= opcion_dos:
        print("Es mayor o igual")
print("fin.")
  
######################

"""