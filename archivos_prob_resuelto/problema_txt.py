#2 listas, una con nombres otra con apellidos
nombres = ["Lucas","Matias","Camila","Pedro","Roberto"]
apellidos = ["Dalto","Zing","Dalto","Robetix","tarado"]

#Registrar y crear  esta información en un TXT de forma óptima

with open("archivos_prob_resuelto\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n-----------\n") for n,a in zip(nombres,apellidos)]
    