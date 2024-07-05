
def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    return a/b


print("Escribe dos numeros")
num1 = float(input())
num2 = float(input())

while(True):
    print("¿Qué operación quieres hacer?")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    op = int(input())

    if op == 1:
        print(sumar(num1,num2))
        break
    elif op == 2:
        print(restar(num1,num2))
        break
    elif op == 3:
        print(multiplicar(num1,num2))
        break
    elif op == 4:
        print(dividir(num1,num2))
        break
    else:
        print("")
        print("Elige un valor válido")
        print("")

