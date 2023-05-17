class Coche():
    
    def desplasamiento(self):
        print("Me desplazo utilizando 4 ruedas")
    
class Moto():
    
    def desplasamiento(self):
        print("Me desplaso en 2 ruedas")
        
class Camion():
    
    def desplasamiento(self):
        print("Me despalso utilizando 6 ruedas")

#-----------METODO DEL FUNCIONAMIENTO DEL POLIMORFISMO, DECLAROMOS UN ELEMENTO GENERICO (vehiculo)
def desplasamientoVehiculo(vehiculo):
    vehiculo.desplasamiento()

#METODOS DE LLAMADO DESPLAZAMIENTO /O COMPORTAMIENTO 
# miVehiculo= Moto()
# miVehiculo.desplasamiento()

# miVehiculo2=Camion()
# miVehiculo2.desplsamiento()

# miVehiculo3=Coche()
# miVehiculo3.despalsamiento()

#----------APLICAMOS EL POLIMORFISMO
miVehiculo=Camion()
#miVehiculo=Moto()
desplasamientoVehiculo(miVehiculo)