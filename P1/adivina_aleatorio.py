import random

def adivina(min,max):
    numero = random.randint(min,max)
    return numero

def comprueba(a,b):
    if(a>b):
        return 1
    elif(a<b):
        return 2
    else:
        return 3


print("Ingrese desde que numero hasta que numero quiere")
min = int(input())
max = int(input())
solucion = adivina(min,max)

print("Le vamos a dar 5 intentos")
bacon = 2
for a in range(1,5):
    print("----Intento: " ,a," ----")
    print("Escriba el numero")
    numero = int(input())
    if(comprueba(numero,solucion)==1):
        print("Debería probar con un numero más pequeño")
    elif(comprueba(numero,solucion)==2):
        print("Debería probar con un numero más grande")
    else:
        print("COORRECCTOOOOO!!")
        print("Su número era: ",numero," y la solución era: ",solucion)
        bacon = 50
        break
    
if bacon == 2:
    print("Mala suerte caballero, la solución era: ",solucion)
        

