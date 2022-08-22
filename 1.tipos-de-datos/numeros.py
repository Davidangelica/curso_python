


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