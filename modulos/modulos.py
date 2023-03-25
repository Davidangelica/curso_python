import modulo_de_funciones as funs # el as es para asignarle un nombre al modulo, o a una funcion que queramos
from modulo_de_funciones import num_par #importamos una funcion en especifico
from modulo_de_funciones import saludar as saludo_normal,saludo_raro  # con el from lo que hacemos es importar funciones en especifico
import sys


# las funciones importadas se transforman en metodos 

saludo = funs.saludar('juan')
print(saludo)

saludo = saludo_normal('flinga')  # si importamos una funcion en especifico sigue siendo una funcion
print(saludo)

saludo2 = saludo_raro('pepe')
print(saludo2)

#con el __name__ podemos ver el nombre original de la funcion
print(saludo_normal.__name__)

num_pares = num_par(2,5,4,7,66,92)
print(num_pares)


print(sys.builtin_module_names) #con este metodo podemos ver todas los modulos de python 

sys.path.append('c:\\practicas') # de esta forma añadimos un modulo a los modulos de python
print(sys.path) # con path podemos ver las rutas de los modulos de python

import Misfunciones # luego llamamos al archivo que queremos usar que esta en el modulo importado

"""de esta forma llamamos a la funcion, es importante que en el archivo que llamemos solo haya funciones, si hay funciones
asignadas en variables e impresas en pantalla estas se van a visualizar cuando llamemos a la funcion"""
print(Misfunciones.num_primos(10)) 
import funciones.crear_funciones 
frase = funciones.crear_funciones.contraseñas_random(3)
print(frase)                                    