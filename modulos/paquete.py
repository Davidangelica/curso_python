import paquetes.saludo_formal as saludo # aca importamos un modulo del paquete paquetes, para que python lo tome como un paquete es importante que tenga un modulo llamado __init__
saludo = saludo.saludo_formal('pepe')
print(saludo)