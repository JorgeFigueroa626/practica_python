class Telefono:
    def __init__(self) -> None:
        pass
    def llamando(self):
        print("llamando...")
    def Ocupado(self):
        print("ocupando...")
        
class Camara:
    def __init__(self) -> None:
        pass
    def foto(self):
        print("tomado foto...")
        
class Reproductor:
    def __init__(self) -> None:
        pass
    def reproductomusica(self):
        print("reproducion de musica...")
    def reproducirvideo(self):
        print("reproductor de video...")
        
class smartphone(Telefono,Camara,Reproductor):
    #LIBERA ESPACIO EN LA MEMORIA, PERO CONSENSERVA LOS METODOS DE LAS CALSES
    def __del__(self):
        print("telfono apagado")

movil= smartphone()
print(movil.reproductomusica())
