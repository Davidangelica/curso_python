# de esta forma reescribimos un archivo, con 'w' le indicamos que vamos a escribir, la w de write
with open('archivos\\texto.txt','w') as archivo:
    archivo.write('si es el mismo precio me quedo con la 2.0t bk2 sino la 3.8 va ')
    
    # para escribir lineas se hace de esta forma, hay que meter las cadenas en una lista
    archivo.writelines(['\nla 3.8 tiene 300cv ', 'la 2.0t bk2 tiene 275cv'])
    
    # agregamos mas lineas
    
    archivo.writelines(['\nla 3.8 tiene techo electrico ', '\nla 2.0t esta menos equipada'])
