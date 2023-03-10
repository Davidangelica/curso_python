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
    