#manejo de errores con try,except y finally
from miexcepcion import MiExcepcion as err # aca importe mi propia exepcion
def sumar():
    while True: # while true es un bucle infinito, se corta con un break
        a = input('ingrese un numero:')
        b = input('ingrese un numero:')
        try:
            resultado = int(a) + int(b) #primero se ejecuta el try, si falla se ejecuta la expecion 
        except Exception as e: #exception es la clase padre de los errores
            print('te pedi numeros no texto master')
            print(f'esta ocurriendo el error: {e}')
        else: #el else se ejecuta en la caso de que el try no lanze una exepcion, con el except no se ejecuta
            break # el break es para cortar el bucle
        finally:
            print('manejo de exepcion finalizada') # el finally se ejecuta simpre
    return resultado
    


print(sumar())


"""try:
    raise err('error 504')
except:
    print('error de valor')"""