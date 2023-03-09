auto_partes = {'piston': 'motor', 'biela': 'motor', 'intercooler': 'turbo', 'cañerias': 'turbo'}

# iterar solo las key
# (no es por poner la variable key)
for key in auto_partes:
    print(key)
    
# para iterrar todo el diccionario hay que usar la funcion items
# la funcion nos devuleve una tupla

for i in auto_partes.items():
    print(i)
    

for i in auto_partes.items():
    key = i[0] 
    value = i[1]
    print(f'la key {key} tiene el valor {value}')