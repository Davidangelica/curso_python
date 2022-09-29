# funcion basica de suma 

def suma (num1, num2):
    total = num1 + num2
    print(total)

suma(10,20)

#funcion basica para chequear numeros pares
#poner el pass es una buena practica

def num_par_en_lista(num_lista):
    for num in num_lista:
     if num % 2 == 0:
      print('se encuentran numeros pares')
      return True 
    else:
        pass
    print('no hay numeros pares')
    return False


num_par_en_lista([4,5,3,7,9,10])


# arguments y keyword arguments
"""
def func(a,b): #key word argunts posicionales
    #retornar el 5% se la suma entre a y b
    return sum((a,b)) * 0.05
"""
#misma logica utlizando argumentos
#ahora podemos poner todos los argunmentos que queramos 
#args retorna una tupla

def func1(*args):
    return print(sum (args) *  0.05)

func1(15,20)

#keyword arguments
#nos retorna un diccionario 

def func2(**kwargs):
    if 'fruit' in kwargs: 
        print('la fruta escogida es : {}'.format(kwargs['fruit']))
    else:
        print('no hay fruta')

func2(fruit = 'pera', veggie = 'zanahoria' )

#funcion con args y kwargs

def func3(*args, **kwargs):
    print(args)
    print(kwargs)
    print('me gustaria comer {} {} y andar en una {}'.format(args[1], kwargs['comida'], kwargs['moto']))

func3(5,30,10, comida = 'tartas', animal='perro', moto = 'yamaha_r6')


#expreciones lamba, mapas y filtros 

#map
numeros = [1,4,9,11,15]

def func4(num):
    resultado = num**2
    return resultado

for item in map(func4, numeros):
    print(item)


#retornar en forma de lista

print(list(map(func4, numeros)))

#filter
# filtrar numeros pares 
numeros = [10,33,54,78,26,98,14,47,58]

def numeros_pares(num):
    return num%2 == 0


for n in filter(numeros_pares, numeros):
    print(n)
         



#lambda
#Lambda se utiliza como si fuece una funcion pero sin ser una def como tal
print('funciones lambda')

numeros = [1,5,6,9,45,47,88]

al_cuadrado = lambda num: num**2 

print(al_cuadrado(5))

#elevar numeros al cuadrado
print(list(map(al_cuadrado, numeros)))

#filtrar numeros pares 
print(list(filter(lambda num: num%2 == 0, numeros)))


#funciones anidadas 
# las funciones anidadas son funciones dentro de otras funciones

name = 'variable global'

def nombre():
    name = 'david'
    
    def saludar():
        print('hola ' + name)
    saludar()

nombre()

#reasiganacion de una variable global
x = 100

def func():
    global x
    print(f'el valor de x es {x}')
    x = 'la variable x fue modificada'
    print('la variable x a cambiado su valor')

func()
print(x)
