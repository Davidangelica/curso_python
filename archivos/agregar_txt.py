# con la 'a' le indicamos que vamos a añadir texto, la a de append
# cada vez que se ejecute el modulo se va a añadir texto al archivo
with open('archivos\\texto.txt','a') as archivo:
    # usando un bucle para añadir varias lineas 
    for i in range(5):
        archivo.write(f'\n{i+1}guatatatatatat')