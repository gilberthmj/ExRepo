import random

def jugada():
    eleccion = random.choice(['Piedra', 'Papel', 'Tijeras'])
    return eleccion

def decision(u,m):
    if(u == m):
        return 'Es un empate'
    
    if (u=='Piedra' and m=='Tijeras') or (u=='Papel' and m=='Piedra') or (u=='Tijeras' and m=='Papel'):
        return 'Usuario Gana'
    return 'Maquina Gana'

print('')
print('Vamos a jugar')
print('Elige tu jugada: Piedra, Papel o Tijeras')
usuario = input()
maquina = jugada()
ganador = decision(usuario, maquina)
print('La jugada del Usuario fue: '+usuario)
print('La jugada de la Máquina fue: '+maquina)
print('---------------')
print(ganador)
print('')
