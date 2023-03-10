# esta funciones son las integradads por python 

# encontrar el numero mas alto y bajo con las funciones max y min

lista = [1,23,45,78,4]

numero_alto = max(lista)
print(numero_alto)

numero_bajo = min(lista)
print(numero_bajo)

# redondear a los decimales  que pongamos con la funcion round

numero = 12.34854894654

numero_redondeado = round(numero,2) # el segundo parametro es para indicarle la cantidad de decimales que queremos
print(numero_redondeado)

# la funcion booleana nos devuelve false si le pasamos 0, false, un elemneto vacio o nada (none)

lista = []

print(bool(lista))

nombre = 'david'

print(bool(nombre))

# la funcion all nos retorna True si todos los datos son verdaderos 

print(all(['pepe','juan',0]))

# la funcion sum suma todos los itereables 

numeros = list([2,3,8,7,5,11])
suma = sum(numeros)
print(suma)