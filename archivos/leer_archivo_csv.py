import csv
with open("archivos\\datos.csv") as archivo:
    reader = csv.reader(archivo) # el reader es una funciones de el metodo csv, esta funcion lee el archivo y devuelve un obejeto, que lo podemos leer 
    for row in reader:           # linea por linea mediante un for 
        print(row)