import sqlite3
import pandas as pd 

funcion_cubo = lambda n : n**3

# la ventaja de usar el with es que la conexion se cierra sola 
with sqlite3.connect("C:\\curso python\\sql\\northwind.db") as conn:
    conn.create_function("n_al_cubo",1,funcion_cubo)
    cursor = conn.cursor()
    cursor.execute('''
    SELECT *, round(n_al_cubo(Price)) as Precio_al_cuadrado FROM products WHERE Price > 0
   
    '''   
    )
    resultado = cursor.fetchall()
    resultado_df = pd.DataFrame(resultado)
    print(resultado_df)
    