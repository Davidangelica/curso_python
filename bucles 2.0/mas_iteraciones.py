frutas = ['pera', 'manzana','kiwi','melon','anana','frutilla']

#con el continue lo que vamos a hacer es parar el bucle en donde le indiquemos y luego continuar
# de esta forma evitamos un elemento de la lista

for f in frutas:
    if f == 'melon':
        continue
    print(f'me voy a comer una: {f}')

# con la sentencia break lo uqe hacemos es parar el bucle (el else no se ejecuta si hay un break)

for f in frutas:
 print(f'me voy a comer una: {f}')
 if f == 'kiwi':
        break
   
#iterar una cedena
cadena = 'hola soy el pata'

for letter in cadena:
    print(letter)
    
#duplicar numeros es una sola linea 
# primero va la expresion matematica luego el for 

numeros = [1,9,8,7,15]

numeros_duplicados = [x*2 for x in numeros]

print(numeros_duplicados)