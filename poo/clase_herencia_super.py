class Persona():
    def __init__(self, nombre,edad,lugar_residencia):
        self.nombre=nombre
        self.edad=edad
        self.lugar_residencia=lugar_residencia
    def descripcion(self):
        print("Nombre:", self.nombre, "Edad:", self.edad, "Residencia:", self.lugar_residencia)

#CLASE DE HERENCIA SUPER
class Empleado(Persona):
    def __init__(self,salario, antiguedad, nombre_empl, edad_empl, lugar_empl):
        #super().__init__("Luis", 25, "Santa Cruz")
        #INICIA PRIMERO LA CLASE DE LA PERSONA  
        super().__init__(nombre_empl, edad_empl, lugar_empl)
        self.salario=salario
        self.antiguedad=antiguedad
    def descripcion(self):
        super().descripcion()
        print("Salario:", self.salario, "Antiguedad:", self.antiguedad)
        
#Luis=Persona("Luis", 25, "Santa Cruz")
Luis=Empleado(2500,15,"Luis", 25, "Santa Cruz")
Luis.descripcion()

#CONSULTAMOS DE LUIS ES DE LA CLASE PERSONA
print(isinstance (Luis, Persona))