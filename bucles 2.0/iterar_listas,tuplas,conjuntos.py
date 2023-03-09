# la funcion zip nos permite iterar elementos a lo vez
# para esto las variables deben tener la misma cantidad de elementos

motor = ['biela', 'piston', 'block', 'levas', 'valvulas']
turbo = ['turbo','intercooler','cañerias','valvula de alivio','reloj de presion']


for m,t in zip(motor,turbo):
    print(f'los elementos del motor son {m}')
    print(f'los elementos del turbo son {t}')

# la funcion range sirve para iterar en un rango determinado, contando el primer numero pero el ultimo no , si no le aclaramos el rango va a iterar hasta llegar al valor dado

for num in range(5,10):
    print(num)
    
for num in range(10):
    print(num)

#recorrer una lista con su indice 

numeros = [1,5,8,88,4]

for num in enumerate(numeros):
    print(num)

# como nos devuelve una tupla con su indice y su valor, podemos visulizarlo mejor:
# num[0] hace referencia al elmento 1 de la tupla osea el indice proporcionado por la funcion enumerate 
# num[1] hace rejerencia al elemento 2 osea el valor

for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es {indice} y su valor es {valor}')
     

# utilizando el else. El else simpre se va a ejecutar

for num in numeros:
    print(f'el valor actual es: {num}')

else:
    print('fin del bucle')