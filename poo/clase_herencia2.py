class pokemon():
    pass
    def __init__(self,nombre,tipo):
        self.nombre=nombre
        self.tipo=tipo
        
    def descripcion(self):
        return '{} es un pokemon de {}'.format(self.nombre, self.tipo)

class piukachu(pokemon):
    def ataque(self, tipoataque):
        return '{} tipo de ataque {}'.format(self.nombre, tipoataque)
    
class charmander(pokemon):
    def ataque(self, tipoataque):
        return '{} tipo de ataque {}'.format(self.nombre, tipoataque)

nuevo_pokemon=piukachu("lolo", "electrico")
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque('impacto trueno'))