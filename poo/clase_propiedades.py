class Empleado:
    def __init__(self,nombre,salario):
        self.__nombre=nombre
        self.__salario=salario
    def __getnombre(self):
        return self.__nombre
    def __getsalario(self):
        return self.__salario
    
    def __setnombre(self,nombre):
        self.__nombre=nombre
    def __setsalario(self,salario):
        self.__salario=salario
    
    def __detnombre(self):
        del self.__nombre
    def __detsalario(self):
        del self.__salario
    nombre =property(fget = __getnombre, 
                     fset= __setnombre, 
                     fdel= __detnombre, 
                     doc="soy el propietario 'nombre'")
    salario= property(fget=__getsalario)
empleado_uno = Empleado('Luis',3500)
empleado_uno.nombre='martha'
print(empleado_uno.nombre,empleado_uno.salario)

#MUETRA TODA LA DOCUMENTACION
#help(empleado_uno)

# empleado_uno= Empleado('Luis',4000)
# print(empleado_uno.getnombre(),',',empleado_uno.getsalario())
# empleado_uno.setnombre('Jorge')
# print(empleado_uno.getnombre(),',',empleado_uno.getsalario())
    