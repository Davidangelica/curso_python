nombres = ['David','Federico','Alejandro','Flor']
apellidos = ['Angelica','Orazi','Radetic','Gonzales']

with open('problemas_archivos\\nombres.txt','w') as archivo:
       archivo.writelines('los datos son: \n')
       archivo.writelines(f'nombre:{n}---------apellido:{a}\n'for n,a in zip(nombres,apellidos))
       
      
    
    
    