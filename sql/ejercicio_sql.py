import sqlite3
import pandas as pd 
import matplotlib.pyplot as plt 

conn = sqlite3.connect("C:\\curso python\\sql\\northwind.db")
cursor = conn.cursor()

#consulta
query = '''
SELECT ProductName, round(sum(Price * Quantity)) as total FROM OrderDetails od
INNER JOIN Products p ON p.ProductID = od.ProductID 
GROUP BY ProductName
ORDER BY total DESC
LIMIT 10
'''

# con este metedo de la libreria panda leemos la consulta 
top_products = pd.read_sql_query(query,conn)

top_products.plot(x="ProductName", y="total", kind="bar", figsize=(10,5), legend=False)

#titulo del grafico
plt.title("the products most profitable")
# nombre del eje x
plt.xlabel("products")
# nombre del eje y
plt.ylabel("total")
# rotamos las palabras del eje x para que no esten una arriba de otra
plt.xticks(rotation=90)
# mostramos el grafico
plt.show()



# en esta segunda consulta lo que hicimos es ver quien vendio mas cantidad de veces, lo que hicimos con el count(*)
# es contar la cantidad de campos que tiene la tabla orders, al agruparlo por empleado  podemos ver quien tiene mas cantidad de ventas hechas 
query2 = '''
SELECT FirstName || " " || LastName as Employee, count(*) as total FROM orders o 
INNER JOIN Employees e 
ON e.EmployeeID = o.EmployeeID
GROUP BY e.EmployeeID
ORDER BY total DESC
LIMIT 10
'''

top_employees = pd.read_sql_query(query2,conn)
top_employees.plot(x="Employee",y="total",kind="bar", figsize=(10,5) ,legend=False)

 
plt.title("the employees with most sales")
plt.xlabel("employees")
plt.ylabel("sales")
plt.xticks(rotation=90)
plt.show()

