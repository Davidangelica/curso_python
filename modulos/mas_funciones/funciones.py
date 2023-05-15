def contraseñas_random(num):
    char = "abcdefghi"
    num_str = str(num)  #lo convertimos a str para poder hacer un indexado
    num = int(num_str[0])
    c1 = num - 2
    c2 = num - 4
    c3 = num 
    contraseña = f'{char[c1]} {char[c2]} {char[c3]} {num *2}'
    return contraseña, num
