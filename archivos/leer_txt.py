archivo_sin_leer = open('archivos\\texto.txt')

#leer el archivo
archivo = archivo_sin_leer.read()


# leer linea por linea
lineas = archivo_sin_leer.readlines() # el archivo una vez que se abre no se puede utilzar dos veces

# leer una linea en especifico, o la cantidad de caracteres que le pasamos 
linea = archivo_sin_leer.readline()
print(linea) 

# cerrar archivo
archivo_sin_leer.close()