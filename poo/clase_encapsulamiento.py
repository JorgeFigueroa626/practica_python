class Coche():
    #ESPEFICAMOS UN CONSTRUCTOR DE ESTADO INICIALIZADO, DE LAS PROPIEDADES
    def __init__(self):
        self.largo=250
        self.ancho=100
        self.color="rojo"
        #ENCAPSULAMOS LA PROPIEDAD
        self.__ruedas=4
        #COMPORTAMIENTO
        self.__enmarcha=False
    
    #---COMPORTAMIENTO--- #AGREGAMOS UN PARAMETRO DE ENTRADA, "ARRANCAMOS"
    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos
        
        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()
            
        if(self.__enmarcha and chequeo):
            return "El auto se mueve"
        
        elif(self.__enmarcha and chequeo==False):
            return "El auto no se mueve, algo salio mal"
        
        else:
            return "El auto esta parado"
        
    def estado(self):
        print("El largo del auto es" ,micoche.largo, "y el color es" ,micoche.color)
        print("El acho del auto es" ,micoche.ancho, "y el numero de ruedas es" ,micoche.__ruedas)
    
    #ENCAPSULAMOS EL METODO
    def __chequeo_interno(self):
        print("realizo el chequeo interno")
        
        self.gasolina="ok"  
        self.aceite="ok"
        self.puerta="cerradad"
        
        if(self.gasolina=="ok" and self.aceite=="ok" and self.puerta=="cerradad"):
            return True
        else:
            return False

#LA INSTANCIA DEL AUTO
micoche=Coche()

#ARRANCAR EL AUTO
print(micoche.arrancar(True))

#IMPRIME LA INTACIA DEL AUTO
micoche.estado()
#################################################
print("---------------El segundo OBJETO-------------------------")

micoche2=Coche()
print (micoche2.arrancar(False))

#TRATA DE MODIFICAR LAS RUEDAS, IMPOSIBLE, POR ESTA ENCAPSULADA
micoche2.ruedas=5

micoche2.estado()