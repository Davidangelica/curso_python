# funcion simple

def saludar():
    print('hola maestro')

saludar()
    
#funciones con parametros

def sumar(a,b):
    suma = a + b
    print(suma)


sumar(10,15)

def saludo_pro(nombre,sexo):
    sexo = sexo.lower() #convierte todo a minuscula
    if sexo == 'femenino':
        print(f'hola {nombre} reina como andas?')
    elif sexo == 'masculino':
        print(f'hola {nombre} maquinola como andas?')
    else:
        print('xd')

saludo_pro('camila','femenino')

def num_par(num):
    if num % 2 == 0:
        print(f'el numero {num} es par')
    else:
        print(f'el numero {num} es inpar')

num_par(54)  
num_par(91)        
    
# funcion que retorna multiples valores
# esta funcion toma el primer digito del numero que le pasemos, ese numero va a ser el indice para tomar un caracter 

def contraseñas_random(num):
    char = "abcdefghi"
    num_str = str(num)  #lo convertimos a str para poder hacer un indexado
    num = int(num_str[0])
    c1 = num - 2
    c2 = num - 4
    c3 = num 
    contraseña = f'{char[c1]} {char[c2]} {char[c3]} {num *2}'
    return contraseña, num

# al usar el return podemos asignarle una variable al valor retornado por la funcion
# usando desempaquetado lo hacemos de manera mas optima

password, num_usado = contraseñas_random(22)
print(f'la contraseña generada es: {password}\nel numero utilizado es: {num_usado}')

# funcion con *args
# este argunto nos permite utilizar muchos paramatros
# solo se puede utilizar una vez
# despues del args no se puede utilizar otro parametro
# args no es ningun tipo de variable, contienen varios elemntos  pero no forman listas,tuplas etc.

def suma(nombre,*numeros):
    resultado = sum(numeros)
    return nombre, resultado

nombre, sumar= suma('juan',2,65,4,7,8,2)
print(f'hola {nombre} tu suma es igual a {sumar}') 

# usando args pero no como parametro
# de esta forma hacemos lo mismo que arriba pero con la diferecia que podemos utilizar mas parametros en la funcion 

def suma1(ID,numeros):
    return ID, sum([*numeros])

ID,resultado1 = suma1(1,[1,2,3,5,8,4,8,6,8]) # los numeros hay que ponerlos en una lista para que se utilize el parametro
print(f'suma numero {ID}\nel resultado de  la suma = {resultado1}')
    

#forzar argumentos
# esto sirve para cambiar el orden de los parametros, si forzamos uno tenemos que forzar todos

def frase(nombre, apellido, edad):
    return f'hola {nombre} {apellido} tu edad es de {edad} años'

frase_retornada = frase(apellido= 'perez', nombre= 'juan', edad= 20)
print(frase_retornada)

#keywords arguments
# de esta forma por defecto la edad es 20

def frase(nombre, apellido, edad = 20):
    return f'hola {nombre} {apellido} tu edad es de {edad} años'

frase_retornada = frase('juan','perez')
print(frase_retornada)

# aunque nos permite modificarla luego 
frase_retornada = frase('juan','perez', 24)
print(frase_retornada)

# funciones lamba 
# Las funciones lamba son anonimas, osea que no tiene nombre 
# estas funciones la podemos almacenar en variables
# retornan valores automaticamente y ahorran codigo, su utilizan para funciones sencillas

# funcion lamba que multiplica por dos y suma 50

cuenta = lambda x: x * 2 + 50

print(cuenta(5)) 

# utlizando filter

# funcion basica que retorna numeros pares 

def num_par(num):
    if num%2 == 0:
        return True

lista = [22 ,2343 ,456 ,6, 31, 32]

# el filter sirve para pasarle varios elementos a una funcion, hace como un bucle porque va recorriendo un arreglo 

numeros_pares = filter(num_par, lista)

# si solo imprimimos nos devulve un objeto filtrado, en este caso (<filter object at 0x000001B73A67F2B0>)
print(numeros_pares)

# hay que meterlo en una lista
print(list(numeros_pares))

# hacindo lo mismo pero con lamba

lista = [1,22,4,8,66,51]

numeros_pares = filter(lambda num: num%2 == 0,lista)
print(list(numeros_pares))