import math

class Pastel:
    def __init__(self,ingredientes):
        self.ingredientes=ingredientes
        
    def __repr__(self):
        return f'pastel({self.ingredientes !r})'
    @classmethod
    def Pastel_chocolate(cls):
        return cls(['harina', 'lecha','chocolate'])
    @classmethod
    def Pastel_vainilla(cls):
        return cls(['harina', 'lecha','vainilla'])
    
#print(Pastel.Pastel_chocolate())

#-------------CLASE ESTATICO----------------
class Pastel:
    def __init__(self,ingredientes, tamaño) -> None:
        self.ingredientes=ingredientes
        self.tamaño= tamaño
    def __repr__(self) -> str:
        return (f'Pastel({self.ingredientes}, 'f'{self.tamaño})')
    def area(self):
        return self.tamaño_area(self.tamaño)
    @staticmethod
    def tamaño_are(A):
        return A ** 2* math.pi
    
nuevo_pastel= Pastel(['harina', 'azucar','leche','crema'],4)
#print(nuevo_pastel.tamaño)
print(nuevo_pastel.tamaño_are(5))