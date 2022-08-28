


from operator import truediv
from random import seed
from traceback import print_tb


micadena = "hello word"

# INDEXADO
# el indince siempre arranaca de cero,  el resultado va a dar l
print(micadena[2])    

# INDEXADO INVERSO
# el indice arranca a la inversa, inicia desde -1
# el resultado va a dar d

print(micadena[-1])

# SLICING
# sirve para agarrar determinados indices 
# en el ejemplo estariamos agarrando desde la "h" a la "l"

print(micadena[0:3])

# [star:stop:step]
# el resultado seria hlo
print(micadena[0:6:2])

# Propiedades de cadenas 
# Son imutables
# Asi cambiamos los caracteres (en el ejemplo las ultimas dos)
# No se pueden sumar

name = "pan"
ultimas_letras = name[1:] 

# ahora concatenamos y nos da "zan"

print('z' + ultimas_letras)

# Multiplicar caracteres 

letra = 'z'
letra = letra * 10

print(letra)

# Seperar palabras 

x = 'hola mundo'
x = x.split()

print(x)

# Separar por letra 

x = 'hola mundo'
x = x.split('o')

print(x)

# Formateo de impresion de cadena de texto 

# Funcion format se asigna el formateo en las "{}"

print('esta es una cadena de {}'.format('TEXTO'))

print('Esta {} {} {}'.format('es','una','cadena'))

# Con indices 

print('Esta {0} {1} {2}'.format('es','una','cadena'))

# Asiganando variables 

print('Esta {e} {u} {c}'.format( e ='es',u= 'una',c ='cadena'))

# Formateo de float 

resultados = 100/888

print("los resultados son {}".format(resultados))

# redondear floats
# en el ejemplo la precisión es 1.3

print("los resultados son {r:1.3f}".format(r = resultados))

# Acortar formats

nombre = "eric"
edad = 22 

print(f"hola me llamo {nombre} y tengo {edad}")


# listas propiedades

mi_lista = [1,2,3]

print (mi_lista)

# Podemos poner cualquier tipo de objeto
#los indices arrancan de 0
# Las listas son mutables

mi_lista = ['cadena',2,3]

print(len(mi_lista))     # el len sirve parar saber cuantos objetos hay, en este caso 3


print (mi_lista[1:])    # el resultado seria 2, 3

# las listas se pueden sumar 

lista_1 = ['uno', 'dos', 'tres']
lista_2 = ['cuatro', 'cinco']

nueva_lista = lista_1 + lista_2

print(nueva_lista)

# Modificamos el indice 0

nueva_lista[0] = 'david'

print(nueva_lista)

# la función append nos permite concatenar 

nueva_lista.append('jose')
print(nueva_lista)

# La función pop nos permite remover un elemnto de la lista 

nueva_lista.pop(5)
print(nueva_lista)

item_popeado = nueva_lista.pop(4)
print(item_popeado)               # Mostramos solo el item popeado


# tambien podemos usar indices negativos

item_popeado2 = nueva_lista.pop(-2)
print(item_popeado2)

# ordenar listas 
# La función sort nos permite ordenar listas 

lista_a = ['e', 'f', 'j', 'k','l']
lista_b = [2,1,7,6]

lista_a.sort()
print(lista_a)

lista_b.sort()
print(lista_b)

# con la función reverse ordena al reves

lista_b.reverse()
print(lista_b)

# Diccionarios

mi_diccionario = {'llave1':'valor1', 'llave2':'valor2' }

print(mi_diccionario)

# Ahora si llamamos una llave nos va a dar el valor que correspondiente

print(mi_diccionario['llave1'])

# ejemplo mas logico

precios_ropa = {'campera': 4000 , 'remera' : 1500 , 'zapatillas' : 8000}

print(precios_ropa['zapatillas'])

# Se pueden incluir listas en los diccionarios 

precios_ropa = {'campera': ['azul', 'negra'] , 'remera' : ['amarillas', 'blancas', 'negras'] , 'zapatillas' : ['negras', 'blancas']}

print(precios_ropa)

print(precios_ropa['campera'][1])

# La propiedad upper cambia a mayúsculas 

print(precios_ropa['campera'][1].upper())

# asi sobrescribimos un diccionario

precios_ropa['jeans'] = 1500

print(precios_ropa)

print(precios_ropa['jeans'])

# La función keys sirve para ver las llaves que tenemos en el diccionario

print(precios_ropa.keys())

# y values para los valores 

print(precios_ropa.values())

# funcion items para ver los pares

print(precios_ropa.items())

# tuplas
# son parecidas a las listas con la diferencia de que son inmutables
# se utiliza en el caso de que no queramos modificar los elementos que contenga

t = (1, 2, 3)

l = [1, 2, 3]

print(type(t))  # la funcion type nos indica que tipo de clase es

# podemos aplicar indices

print(t[0:2])

# Contador

remeras = ('negra', 'negra', 'roja')

print(remeras.count('negra'))  # la funcion count cuenta cuantos objetos iguales hay 

# funcion index, nos dice en que indice se encuntra el objeto dicho

print(remeras.index('roja'))


# sets
# un set tiene valores unicos 
# no tiene orden

mi_set = set() 

# para añadir elemontos a un set se utiliza la funcion .add

mi_set.add(1)

print(mi_set)

# el set utiliza cuando pj tenemos muchos elementos repetidos en una lista

num = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,3]

print(set(num)) #como el set agarra un unico elemento nos mostraria 1, 2, 3

# valores boleanos 
# nos permiten declarar verdadero o falso

print (4<5) #true
print (5<4) #false

#comparadores 

# igual se escribre ==

2 == 2   #true
2 == 3   #false 
print('carlos' == 'pepe') #false
print(2 == '2')  #false 


# desigual 

print(2 != 2)  #false 

# mayor 

print(5 > 4)

# menor 

print(4 < 5)

# mayor o igual, menor o igual

print (5 >= 5)
print (4 <= 5)


# Encadenado de comparadores 
# #se utilizan operadores logicos para combinar comparaciones
# operadores logicos: and, or , not 

print(4 < 5 and 5 >= 5) # si 4 es menor que 5 Y 5 mayor o igual que 5, true  {true and true : true} {true and false : false} {false and false : false}

print(4 < 5 or 5 >= 5) # si 4 es menor que 5 O 5 mayor o igual que 5, true, con que una de la condicion se cumpla da true

print(not 2 == 2) # el not devulve el resultado iverso en este caso false

print (not 2 == 3) # en este caso true 

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