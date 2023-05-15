import pandas as pd 

#leyendo csv con pandas
df1 = pd.read_csv('archivos\\datos.csv') #la variable df hace referncia a dataframe, el dateframe se compone de filas y columnas
df2 = pd.read_csv('archivos\\datos.csv')
print(df1) 

print()

# visulizando solo los nombres
nombres = df1['nombre']
print(nombres)

print()

# editando los encabezados
df = pd.read_csv('archivos\\datos.csv',names=['name', 'lastname', 'age'])
print(df)

print()

# ordenando de forma ascendente
df_ordenado = df.sort_values('age')
print(df_ordenado)

print()

#ordenando de forma descendente
df_ordenado = df.sort_values('age',ascending=False) #modificando el parametro ascending a falso se va ordenar de forma desendiente
print(df_ordenado)

print()

#concatendo dateframe 

dataframe_concatenado = pd.concat([df1,df2])
print(dataframe_concatenado)

print()

# accediendo a filas del df

primeras_filas = df.head(2) #le tenemos que pasar como paramatero el numero de fila, muestra desde el la primera hasta el numero que le pasamos 
print(primeras_filas)

print()

#accedindo filas pero desde la ultima 

ultimas_filas = df.tail(1)
print(ultimas_filas)

print()

#ver la cantidad de filas y columnas que tiene el df

filas_columnas_totales = df.shape #esto nos devulve una tupla, primero la cant de filas y segundo la cantidad de columnas
print(filas_columnas_totales)

print()

#utilizando desempaquetado para tener una variable para cada valor

filas_totales, columnas_totales = filas_columnas_totales
print(f'hay {filas_totales} filas')
print(f'hay {columnas_totales} columnas')

print()

# obteniendo data estadistica del dataframe

info_df = df.describe()
print(info_df)

print()

#accediendo a un elemento en especifico del df con loc
#ponemos la fila y el valor que queres saber
elemento_especifico = df.loc[1,'age'] #loc es un atributo 
print(elemento_especifico)


#accediendo a un elemento en especifico del df con iloc, iloc significa que funciona con indices
#con iloc accedemos al el elemnto especificando la fila y la columna

elemento_especifico = df.iloc[1,2] #iloc es un atributo 
print(elemento_especifico)

#accediendo a todos los valores de un elemento
#mediente slicing le indicamos todas las filas de la columna 1

apellidos = df.iloc[:,1]
print(apellidos)

#accediendo a todos los datos de una fila

fila_1 = df.iloc[1,:]
print(fila_1)

print()

#accediendo a las filas con una condicion

"""edad_mayor_30 = df.loc[df['age']>30,:]
print(edad_mayor_30)"""
