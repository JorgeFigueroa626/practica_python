import csv
 
with open("archivos\\datos.csv") as archivos:
     reader = csv.reader(archivos)
     for row in reader:
         print(row)