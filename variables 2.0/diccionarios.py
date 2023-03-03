# funcion dict
diccionario = dict(nombre = 'david', apellido = 'angelica', edad = 20)
print(diccionario)

# las tuplas pueden ser claves pero las listas no 
diccionario = {('deportivo', 'coupe'):'genesis'}
print(diccionario)

# con los sets pasa lo mismo que con las listas expto que utilizemos la funcion frozenset

piezas = frozenset({'piston', 'biela'})

diccionario = {'motor': piezas}
print(diccionario['motor'])

#creando diccionarios con fromkeys
#esta lo que hace es crear datos con valores vacios

diccionario = dict.fromkeys(['david','angelica', 20])
print(diccionario)

#este metetdo funciona iterando asi que si le pasamos una cadena, este va a crear un valor vacio para cada caracter

diccionario = dict.fromkeys('auto')
print(diccionario)

# el primer dato va ser el iterable, el segundo el valor

diccionario = dict.fromkeys('abcd',1000)
print(diccionario)

#ejemplo con lista, cada elemnto va a agarrar el valor que le pasemos

diccionario = dict.fromkeys(['biela', 'piston'], 'motor')
print(diccionario)