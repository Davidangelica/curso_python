# declaraciones if y elif 

hambre = True 

if hambre :
    print ('tengo hambre')

manzana = False 

if manzana : 
    print ('hay manzana')
    
else:
     print ('no hay manzana') 

 

sed = True 
calor = True

# calor
if calor:
    print('hace calor')

elif sed and calor:
    print('tengo sed y calor')

else:
    ('estoy bien')

# sed y calor

if calor and not sed:
    print('hace calor')

elif sed and calor:
    print('tengo sed y calor')

else:
    ('estoy bien')


# ciclos for 

# hacemos un iteado de la lista
listafor = [1,2,3,4,5,6,7,8,9,10]

for num in listafor:   # num representa a cada item que se encuntra dentro de la listo (puede ser cualquier nombre)
    print (num)

for num in listafor:
    print('hola')      # se van a imprimir 10 holas seguidos porqwue hay 10 items 


# buscar numeros impares y pares 

for num in listafor:
    if num % 2 == 0:
        print(f'el numero: {num} es par' )
    else : 
        print (f'el numero: {num} es impar')


# suma con ciclos for 
# se van a ir sumando los item de la listafor

sumalista = 0

for num in listafor:
    sumalista = sumalista + num
    print(sumalista)


# ciclos for con cadenas de texto 

# iteado 

listafor = 'hola mundo'

for letter in listafor :
    print(letter)


# desenpaquetar pares 

tuplafor = [(1,2), (3,4), (5,6)]

print(len(tuplafor)) # nos dice cuantos elementos hay 

for item in tuplafor:
    print(item)

# desempaquetado de una tupla 
# en este caso a,b por son items con pares 

for (a,b) in tuplafor:
    print(a)
    print(b)


# cilos for con diccionarios 
# imprimimos solo las llaves
d = {'A':1, 'B':2, 'C':3 }

for item in d:
    print(item)

# imprimimos los items con la funcion .items()

for item in d.items():
    print(item)

# para imprimir las llaves y el  valor
# hacemos un desempaquetado en cual a = llave y b = valor
for llave, valor in d.items():
    print (f'la llave {llave}')
    print (f'tiene de valor  {valor}')


# imprimir solo el valor con la funcion .values()

for value in d.values():
    print(value)


# ciclos while
# los bloques while se van a seguir ejecutando una linea de codigo hasta que el bloque sea true 

""""
x = 0             # este ciclo while es infinito 

while x < 5 :

 print (f"el valor actual de {x} es : ")
"""

x = 0            

while x < 5 :

 print (f"el valor actual de x es : {x}")

 x += 1      #ahora tenemos una condicion, cada vez que se repita el ciclo se ve a sumar uno a la x por ende va a parar  cuando llegue a 4
else:
    print('x no es mayor que 5') # el else se ejecuta al finalizar el ciclo 


# palabras claves utiles 
# break
# pass
# continue

x = [1,2,3]
# el pass sirve para pasar el error 
for item in x:
    #comentario  
    pass
print('fin')

x = 'david'

# el continue sirve para saltearse un item, en este caso la i
for letter in x:
    if letter == 'i':
     continue
    print(letter)

# el break corta la cadena, en este caso cuando llega al ad se corta 

for letter in x:
    if letter == 'v':
        break 
    print(letter)

# operadores utilies 

#range 
# con esta funcion podemos crear numeros con la cantidad de indices que pongamos

milista=[1,2,3]

for num in range(10):
    print(num)

# tambien podemos hacerlo con paso 
for num in range(0,11,2):
    print(num)


#creamos una lista con la funcion range

print(list(range(5)))

#contador de indeces 
contador_de_indices = 0

palabra = 'hola'

for letter in palabra:
    print(palabra[contador_de_indices])
    contador_de_indices += 1 

#la funcion enumerate nos marca los indeces de cada item

for item in enumerate(palabra):
    print(item)

#separar por pares

for index, letter in enumerate(palabra):
    print(index)
    print(letter)
    print('\n')

#emparejar dos listas 
# la funcion zip toma el menor indice posible, si tuviera una lista mas con 5 items pj, solo va a tomar los 3 primeros 

milista1 = [1,2,3]
milista2 = ['a','b','c']

for item in zip(milista1, milista2):
    print(item)

#cambiar el tipo de variable ingresada mediante un input
"""""
resultado = input('ingrese un numero:  ')

print(type(int(resultado)))
"""""
#comprension de listas 
#transformamos una cadena en una lista

mi_cadena = 'pepe'
mi_lista  = []

for letter in mi_cadena:
    mi_lista.append(letter)
print(mi_lista) 

#crear listas utilizando ciclos for 

mi_lista = [x for x in range(0,11)]
print(mi_lista)

#pequeño algortimo de conversion de forma optimizada 

celsius = [0, 10, 20, 34.4]

fahrenheit = [((9/5) * temp + 32) for temp in celsius]
print(fahrenheit)

#algoritmo de conversion de forma clasica 

fahrenheit = []

for temp in celsius:
    fahrenheit.append(((9/5) * temp + 32))
print(fahrenheit)