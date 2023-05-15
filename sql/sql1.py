import sqlite3
import pandas as pd 

fun_potenciacion = lambda n : n**3 # funcion para elevar un numero al cubo

conn = sqlite3.connect("C:\\curso python\\sql\\northwind.db") # conectamos con la base de datos

conn.create_function("fun_potenciacion",1,fun_potenciacion) # el primer parametro es para poner el nombre a la funcion en la base de datos
                                                            # el segundo parametro es para indicar cuantos parametros va a tener la funcion
                                                           # el tercer parametro es para indicar que funcion va a usar 
                                                           
# el cursor realiza y alamacena la consulta (no el base de datos) sino que en el mismo cursor
cursor = conn.cursor()

# aca hacemos una consulta 
cursor.execute('''
SELECT * FROM Products
'''    
)
#el fetchall sirve para obtener los resultados de una consulta que estan en el cursor 
resultados = cursor.fetchall() # esto devulve una lista con todos los valores de la tabla de sql
result_dataframe = pd.DataFrame(resultados) # con la libreria pandas podemos convertir el resultado en un dataframe, para poder verlo mejor 
print(result_dataframe)

# con el commit guardamos los cambios en la base de datos
conn.commit()

# cerramos el cursor y la conexion, es importante hacerlo para liberar recursos 
cursor.close() 
conn.close()
