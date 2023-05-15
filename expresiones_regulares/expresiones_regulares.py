import re # modulo de expresiones

texto = '''hola como andan?
aca tomando una birrita de 5. pe con mani y
con mi amigo el pata55. abab'''

resultado = re.search('hola',texto) # buscar una palabra en el texto, si hay mas de una devuelve la ultima

resultado = re.findall('con', texto, flags=re.IGNORECASE) # pone en una lista todas las veces que se repite una palabra, con el parametro flags podemos usar otra funcion, en esta caso ignorar mayusculas

# \d busca digitos numericos del 0 al 9 
resultado = re.findall(r'\d', texto)

# \D busca todo lo que no son digitos numericos del 0 al 9 
resultado = re.findall(r'\D', texto)

# \w busca todo los caracteres alfanumericos [a-z, A-Z, 0-9, _]
resultado = re.findall(r'\w', texto)

# \W busca todo lo que no son caracteres alfanumericos 
resultado = re.findall(r'\W', texto)

# \s busca espacios en blanco -> salto de lineas, espacios y tabs
resultado = re.findall(r'\s', texto)

# \S busca todo lo que no esta en espacios en blanco
resultado = re.findall(r'\S', texto)

# . busca todo menos saltos de linea 
resultado = re.findall(r'.', texto)

#\n busca saltos de linea
resultado = re.findall(r'\n', texto)

#\ cancelerar caracteres especiales, cancelando la funcion del punto y buscando puntos
resultado = re.findall(r'\.', texto)

# buscar una sentencia de datos, en este caso: un numero seguido de un punto y de un espacio, si no se da la sentencia que le indicamos muestra una lista vacia
resultado = re.findall(r'\d\.\s', texto)

# ^  para ver si una palabra esta al principio de una linea 
resultado = re.findall(r'^hola', texto) # de esta forma solo no sirve para buscar una palabra de la primera linea

#si en el paramatro flags le ponemos el .m va a tomar la cadena como multilineas y de esta forma podemos buscar todas las  palabras que esten en el principio de otra linea 
resultado = re.findall(r'^aca', texto, flags=re.M)

#$ buscamos el final de una linea
resultado = re.findall(r'y$', texto, flags=re.M)

# {n} busca n cantidad de veces el valor de la izquierda, en este caso va a buscar dos numeros seguidos
resultado = re.findall(r'\d{2}', texto)

# {n,m} busca como minimos n cantidad de veces y como maximo m cantidad de veces
resultado = re.findall(r'\d{1,2}', texto)

# buscar en conjunto, en este caso va a devolver ab cada dos ab que encuentre
resultado = re.findall(r'(ab){2}', texto)

# | operador or, busca una cosa o la otra 

resultado = re.findall(r'5|hola', texto)

print(resultado)

# ejercicio practico 1

# la cadena en la que se buscan los patrones
text = 'hoy es 02/04/2023 y se conmemora el Día del Veterano y de los Caídos en la Guerra de las Malvinas'

# el remplazo que queremos hacer
remplace = 'feriado'

# el patron que vamos a usar para el remplazo
pattern = r'\d{2}/\d{2}/\d{4}'

# buscamos con el patron, encontramos y remplazamos por la variable dada 
new_text = re.sub(pattern,remplace,text) # la funcion sub se utliza para remplazar
print(new_text)

#ejercicio practico 2

text2 = 'remplazando aeiou todas las vocales por el asterisco'
new_text2 = re.sub('[aeiou]','*', text2) # se pone en [] porque sino buscaria como una palabra
print(new_text2)

#ejercicio practico 3

email = 'exaple@example.com'

"""puede ser de la a-z de la A_Z del 0-9, todo lo que no sea un espacio en linea, el mas nos busca una o mas coincidencias,
antes del @ tiene que haber por lo menos un caracter que cumple las condiciones del corchete, despues del @ la misma condicion,
despues buscamos especificamnete un punto, y por ultimo buscamos de la a-z A-Z por lo menos dos veces
"""
pattern = '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._+-]+\.[a-zA-Z]{2,}'
# con match buscamos coincidencias
result = re.match(pattern,email)

# verificamos si el valido
if result:
    print('mail valido')
else:
    print('mail invalido')
    
#ejercicio practico 4

web = 'este es un ejemplo de pagina web: https://www.example.com y tambien podemos encontrar : https://www.genesisv6.com'
# ? es para mostrar https si aprece sino no pasa nada, se pone asi porque puede empezar por http
pattern = 'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
result = re.findall(pattern,web)
print(result)

#ejerecicio practico 5

# ocultando un numero de telefono

numero = 'hola mi numero es: +54 11 6666-4545'
remplace = 'numero oculto'
pattern = r'\+\d{2}\s\d{2}\s\d{4}-\d{4}'
resultado= re.sub(pattern,remplace,numero)
print(resultado)