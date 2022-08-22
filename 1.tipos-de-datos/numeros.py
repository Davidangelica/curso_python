
from operator import le
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


