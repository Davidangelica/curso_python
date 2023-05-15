# de esta forma el archivo se abre y se ejecta lo que indiquemos y se cierra
with open('archivos\\texto.txt') as archivo:
    print('el archivo se abrio correctamente')
    print(archivo.read())