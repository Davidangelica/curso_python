class perro():

    def __init__(self,raza,nombre,manchas):
        #atributos
        self.raza = raza 
        self.nombre = nombre

        #esperamos un valor booleano
        self.manchas = manchas

perro1 = perro(raza = 'galgo', nombre = 'tina', manchas = False)

#herencia y polimorfismo 


class animal():
    def __init__(self):
        print('hemos creado un animal')

    def quien_soy(self):
        print('soy un animal')
    
    def comer(self):
        print('estoy comiendo')

class perro(animal):
    def __init__(self):
        animal.__init__(self)
        print('perro creado')

    def quien_soy(self):
        print('soy un perro')

miPerro = perro()

miPerro.quien_soy()