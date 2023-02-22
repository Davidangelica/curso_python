#promedio de horas
este_curso = 1.5
min_otros = 2.5
promedio = 4
max_otros = 7

#crudo
tiempo_crudo_promedio = 5
crudo_dalto = 3.5
#porcentajes a comparacion de otros cursos
mas_rapido_otros = 100 - (este_curso / min_otros) * 100 
print(f'este curso es %{round(mas_rapido_otros)} mas rapido que el minimo de la media')

mas_lento_otros = 100 - (este_curso / max_otros ) * 100
print(f'este curso es %{round(mas_lento_otros)} mas rapido que el maximo de la media')
 
promedio_otros = 100 - (este_curso / promedio ) * 100 
print(f'este curso es %{round(promedio_otros)} mas rapido que el promedio de la media') 

#porcentajes de material recortado