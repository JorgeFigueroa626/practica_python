"""
    # EJERCICIO DE CONDICIONALES

########
edat=12
if edat >= 15:
    print("podes pasar")
else:
    print("no podes pasar")
    print("myu mal")
#print("no forma de ningun condicional")

#######

contraseña_alamcenadaDB="pedro"
contraseña_alamcenadaDB="toto"

if contraseña_alamcenadaDB == contraseña_alamcenadaDB:
    print("INICIA NSESSION..")
else:
    print("no podes pasar")
    print("myu mal")
#print("no forma de ningun condicional")


############

## if anidado elif

ingreso_mensual=9000
gasto_mensual=8000
if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("estas bien")
    else:
        print("y estas gastanto mucho, te alacanza")

elif ingreso_mensual > 1000:
    print("estas bien latina")
elif ingreso_mensual > 500:
    print("estas bien bolivia")
elif ingreso_mensual > 200:
    print("estas bien venesuela")

else:
    print("estas pobre")





# AND
#Resultado = 10 ==10 & 10=10

Resultado = True & True # True
Resultado2 = False & True # False
Resultado3 = True & False # False
Resultado4 = False & False # False

# OR
Resultado6 = 10 == 9 | 10==10

Resultado5 = True | True # True
Resultado6 = False | True # True
Resultado7 = True | False # True
Resultado8 = False | False # False

# NOT
Resultado9 = not 2==2

Resultado9 = not True # False
Resultado10 = not False # True

#print(Resultado9)

######################

print("****************")
print("Opciones a condicionales")
print("****************\n")

print("Menu de obciones\n")
print("opcion 1 condicional (and)")
print("opcion 2 condicional (or)")
print("opcion 2 condicional (not)\n")

opcion=int(input("¿Eliga la opcion?: "))

if opcion == 1:
    print("\n Convertir condicional AND. \n")

    opcion_uno=int(input("¿Eliga un numero mayor a 2 y menor a 5?: "))

    if opcion_uno > 2 and opcion_uno <5:
        print("El numero ", opcion_uno, " cumple con la condicion\n")
    else:
        print("El numero ", opcion_uno, " No cumple con la condicion\n")

elif opcion == 2:
    print("\n Convertir condicional OR. \n")

    opcion_dos=input("¿Eliga una palabla 'si' o 'yes'?: ")
    opcion_dos= opcion_dos.lower()

    if opcion_dos == "si" or opcion_dos == "yes":
        print("La condicion ", opcion_dos, " cumple con la condicion\n")
    else:
        print("La condicion ", opcion_dos, " No cumple con la condicion\n")

elif opcion == 3:
    print("\n Convertir condicional NOT. \n")

    opcion_tres=int(input("¿Eliga un numero igual a 5: "))

    if  not opcion_tres == 5:
        print("\n La condicion ", opcion_tres, " es diferente y si cumple la condicion\n")
    else:
        print("\n La condicion ", opcion_tres, " es igual a 5 y No cumple con la condicion\n")

else:
    print("Opcio no disponible")

print("fin.")

####

print("****************")
print("Sistema de control de vacaciones")
print("****************\n")

nombre_empl=input("Ingrese el nombre del empleado: ")
clave_dptm=int(input("Ingrese la clave del dptm: "))
antiguedad_empl=float(input("Ingrese los años de servicio del empleado: "))

if clave_dptm ==1:
    if antiguedad_empl >=1 and antiguedad_empl <= 2:
        print("El empleado ", nombre_empl, " tiene 6 dias vacaciones")
    if antiguedad_empl >=2 and antiguedad_empl <= 6:
        print("El empleado ", nombre_empl, " tiene 12 dias vacaciones")    
    if antiguedad_empl >=7:
        print("El empleado ", nombre_empl, " tiene 24 dias vacaciones")

elif clave_dptm ==2:
    if antiguedad_empl >=2 and antiguedad_empl <= 3:
        print("El empleado ", nombre_empl, " tiene 7 dias vacaciones")
    if antiguedad_empl >=3 and antiguedad_empl <= 6:
        print("El empleado ", nombre_empl, " tiene 14 dias vacaciones")    
    if antiguedad_empl >=7:
        print("El empleado ", nombre_empl, " tiene 28 dias vacaciones")

elif clave_dptm ==3:
    if antiguedad_empl >=1 and antiguedad_empl <= 2:
        print("El empleado ", nombre_empl, " tiene 8 dias vacaciones")
    if antiguedad_empl >=2 and antiguedad_empl <= 6:
        print("El empleado ", nombre_empl, " tiene 16 dias vacaciones")    
    if antiguedad_empl >=7:
        print("El empleado ", nombre_empl, " tiene 32 dias vacaciones")

else:
    print("La clave del dptm no existe")
print("Fin")
 

####

print("****************")
print("Determinar si es par o impar ")
print("****************\n")

numero = int(input("intoducir numero par: "))

if numero%2==0:
    print("El numero ", numero, " es par")
elif  numero%2==1:
    print("El numero ", numero, "es impar")

####

print("****************")
print("Determinar cual es mayor ")
print("****************\n")

numero1 = int(input("intoducir numero1: "))
numero2 = int(input("intoducir numero2: "))
numero3 = int(input("intoducir numero3: "))
num=0
if numero1 > numero2 and numero1 > numero3:
        print("El numero ", numero1, " es mayor")
else:
    if numero2 > numero3:
        print("El numero ", numero2, " es mayor")
    else:
        if numero2 < numero3:
            print("El numero ", numero3, " es mayor")

###

nombre = "Hola "
nombre += input("Escribe tu nombre: ")

print(nombre, ", este es el incremento y decremento de una variable \n")

print("incremento")
x=1
print("El valor inicial de x es: ", x)
x+=1
x+=1
x+=1
x+=1
print("El valor final de x es: ", x, "\n")

print("disminucion")
print("El valor inicial de x es: ", x)
x-=1
x-=1
x-=1
x-=1
print("El valor final de x es: ", x, "\n")

####

print("Menu de obciones\n")
print("1 Sumar")
print("2 Restar")
print("3 Multiplicar")
print("4 Division\n")

opcion=int(input("¿Eliga la opcion?: "))

if opcion == 1:
    print("\n Elegiste sumar \n")

    opcion_uno=int(input("Introducir el primer numero: "))
    opcion_dos=int(input("Introducir el segundo numero: "))

    numero=opcion_uno + opcion_dos
    print("\n La suma es:",numero, " \n")

elif opcion == 2:
    print("\n Elegiste restar \n")

    opcion_uno=int(input("Introducir el primer numero: "))
    opcion_dos=int(input("\n Introducir el segundo numero: "))

    numero=opcion_uno - opcion_dos
    print("\n La resta es:",numero, " \n")

elif opcion == 3:
    print("\n Elegiste multiplicar \n")
    
    opcion_uno=int(input("Introducir el primer numero: "))
    opcion_dos=int(input("\n Introducir el segundo numero: "))

    numero=opcion_uno * opcion_dos
    print("\n La multiplicacion es: ",numero, " \n")

elif opcion == 4:
    print("\n Elegiste division \n")
    
    opcion_uno=int(input("Introducir el primer numero: "))
    opcion_dos=int(input("\n Introducir el segundo numero: "))

    numero=opcion_uno / opcion_dos
    print("\n La division es: ",numero)

else:
    print("Opcio no disponible")

print("fin.")


###

x=0
while x<5:
    print("luis ",x)
    x +=1
print("\nfin")

#####
print("serie fibonachi")
nu1, nu2= 0, 1
while nu2 <=1597:
    print(nu1, nu2, end=" ")
    nu1 = nu1 + nu2
    nu2 = nu1 + nu2
print("\nfin")


#####
print("Opcion de Detencion ,break")
nu1= 0
while nu1 < 10:
    nu1 += 1
    if nu1 == 7:
        break
    print("Valor actual de la variable: ", nu1)

print("Fin del programa, se ejecuto el break")

#####
print("Opcion de continuar")
nu1= 0
while nu1 < 10:
    nu1 += 1
    if nu1 == 7:
        continue
    print("Valor actual de la variable: ", nu1)

print("Fin del programa, se ejecuto el break")


"""