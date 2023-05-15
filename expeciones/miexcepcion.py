
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f'cometiste el siguiente error: {err}')

"""
try:
    raise MiExcepcion('error 2404') # con el raise llamamos a la exepcion
except:
    print('mas atento la proxima') """