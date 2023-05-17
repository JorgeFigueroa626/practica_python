class Vehiculos():
    
    def __init__(self, marca, modelo) -> None:
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
        
    def arrancar(self):
        self.enmarcha=True
    
    def acelerar(self):
        self.acelera=True
    
    def frenar(self):
        self.frena=True
        
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
              self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

print("----------Clase de Camion--------------")
class Camion(Vehiculos):
    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado):
            return "El camion esta cargado"
        else:
            return "No esta cargado el camion"

print("----------Clase de Moto--------------")

class Moto(Vehiculos):
    hcaballito=""
    def caballito(self):
       self.hcaballito="Voy hacer el caballito"
    #SOBRE ESCRIBIMOS EL MOTODO DE ESTADO, AGREGAMOS UN METODO DE CABALLITO
    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
              self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)

print("----------Clase independiente - Hacer Mantenimiento--------------")
class VElectrico(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca,modelo)
        self.autonomia=100
        
    def cargaelectrico(self):
        self.cargado=True

print("----------Return de Moto--------------")
miMoto=Moto("Yamaha", "250")
miMoto.caballito()
miMoto.estado()

print("----------Return de Camion--------------")
miCamion= Camion("Hondad","RRP")
miCamion.arrancar()
miCamion.estado()
print(miCamion.carga(True))

print("----------Clase de herencia multiples, preferencia siempre a la clase de la izquierda (VElectrico)--------------")
class BicicletaElectrica(VElectrico, Vehiculos):
    pass
miBici=BicicletaElectrica("Toyota", "350")