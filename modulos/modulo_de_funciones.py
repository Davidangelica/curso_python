def saludar (name):
    return f'hola {name} espero que tenga un buen dia'

def saludo_raro (name):
    return f'hola {name} estas de rutovich animalovichhhh?'




def numeros_cal (operacion, numeros):
    return operacion, [*numeros]

def calculadora(op,nums):
    cuenta = numeros_cal(op,nums)
    if op == 1:
        
        cuenta = sum(nums)
        
    if op == 2:
        
        resta = []
        rango = len(nums) - 1
        
        for i in range(rango):
            resultado = nums[0] - nums[-1]
            nums.pop(-1)
            nums.insert(0,resultado)
            resta.append(resultado)
            
        cuenta = resta[-1]
    
    if op == 3:
        
        multiplicacion = []
        rango = len(nums) - 1
        
        for i in range(rango):
            resultado = nums[0] * nums[-1]
            nums.pop(-1)
            nums.insert(0,resultado)
            multiplicacion.append(resultado)
            
        cuenta = multiplicacion[-1]
        
    if op == 4:
        
        division = []
        rango = len(nums) - 1
        
        for i in range(rango):
            resultado = nums[0] / nums[-1]
            nums.pop(-1)
            nums.insert(0,resultado)
            division.append(resultado)
            
        cuenta = division[-1]
        
             
    return cuenta

calculadora = calculadora(4,[10,2])
print(calculadora)
    
    
def num_par (*nums):
    pares = []
    for i in nums:
        if i %2 == 0:
            pares.append(i)
    return pares
    
