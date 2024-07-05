

def crea_piramide(deph):
    for i in range(deph):
        print(' ' * (deph - i - 1) + "*" * (2 * i + 1))
        # Explicacion: concatena (espacios vacios) a los asteriscos, pero haciendo *2 por ejemplo hace que aparezcan dos veces
        # por ende en la primera iteración pasa esto: deph=3; i=0; en el primer nivel concatena 2 (espacios en blanco) con 1 asterisco
        # en el segundo nivel deph=3; i=1, concatena 1 (espacio en blanco) con 2 asteriscos y así sucesivamente...




print('Escriba la profundidad de la piramide: ')
deph = int(input())
crea_piramide(deph)
