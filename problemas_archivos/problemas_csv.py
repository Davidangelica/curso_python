import pandas as pd 
df = pd.read_csv('archivos\\datos.csv')

# de esta forma se convierten todos los datos de una columna a str
df['edad'] = df['edad'].astype(str)

#remplazar un valor 
df['edad'].replace('20','21',inplace=True) #inplace = True realiza la operación de eliminado sobre el mismo DataFrame, en lugar de crear y devolver uno nuevo

print(df['edad']) 

#eliminar las filas con objetos vacios
print(df)
df = df.dropna() #con el parametro axis=1 eliminamos columnas
print(df)

#eliminar filas duplicadas

df = df.drop_duplicates()
print(df)

#creando un csv con la dataframe resultante 

df.to_csv('problemas_archivos\\csv_limpio.csv') 