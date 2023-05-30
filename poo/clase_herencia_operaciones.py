class Calculadora:
    def __init__(self,numero) -> None:
        self.n=numero
        self.datos=[0 for i in range(numero)]
        
    def ingresando(self):
        self.datos = [int(input('ingrese datos ' +str(i+1)+ ' = ')) for i in range(self.n)]
        
class operaciones( Calculadora):
    def __init__(self) -> None:
        #LIMITAMOS o CONTROLAMOS LA CANTIADAD DE LA FILA, DEL DATOS ,ELEMENTO
        Calculadora.__init__(self,2)
        
    def suma(self):
        a,b=self.datos
        s= a+b
        print('el resultado es: ',s)
    
    def resta(self):
        a,b=self.datos
        s= a-b
        print('el resultado es: ',s)
        
    def multiplicaion(self):
        a,b=self.datos
        s= a*b
        print('el resultado es: ',s)
        
    def division(self):
        a,b=self.datos
        s= a/b
        print('el resultado es: ',s)
        
    def opr(self):
        a,b=self.datos
        s= a**b
        print('el resultado es: ',s)

class raiz(Calculadora):
    def __init__(self):
        #LIMITAMOS o CONTROLAMOS LA CANTIADAD DE LA FILA, DEL DATO ,ELEMENTO
        Calculadora.__init__(self,1)
        
    def cuadrado(self):
        import math
        a, =self.datos
        print('el resultado es ',math.sqrt(a))
        
# resultado=operaciones()
# print(resultado.ingresando())
# print(resultado.resta())

# resultado=raiz()
# print(resultado.ingresando())
# print(resultado.cuadrado())

#FUNCIONES DE PRUEBA INTEGRADAS- COMPROBAR SI ESTA TRABJANDO CON ESA FUNCION (FALSO o TRUE) 
objeto=operaciones()
#print(isinstance(objeto,operaciones))
#print(isinstance(objeto,raiz))

####OTRO MODO DE PRUEBA, PRIMERO PONIENDO EL METODO DE HIJO, DESPUES EL DEL PADRE
print(issubclass(raiz,Calculadora))