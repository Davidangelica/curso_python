#creando un set con la funcion sets
conjunto = set(['auto', 'motor','chasis'])
print(type(conjunto))

#meter conjunto dentro de otro conjunto
# la funcion frozenset nos permite hacer eso

conjunto1 = frozenset({'motor','biela','piston'})
conjunto2 = frozenset({'turbo','intercooler'})

conjunto3 = {conjunto1, conjunto2}

print(conjunto3)

#teoria de conjuntos 

conjunto1 = {1,2,3,4,5}
conjunto2 = {1,2,3}

# vereificando subconjuntos
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

# vereificando superconjuntos
resultado = conjunto2.issuperset(conjunto1) #false
resultado = conjunto2 < conjunto1 #true

print(resultado)

#verificando si hay algun numero en comun
#este metodo verifica si son iguales los conjuntos, si alguno de los elemntos se repite devuelve false
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)

motor = {'piston','biela'}
sobrealimentacion = {'turbo','intercooler'}

resultado = motor.isdisjoint(sobrealimentacion) # true
print(resultado)

