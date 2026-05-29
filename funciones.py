def pedir_numero():
    while True:
        n = int(input("Ingrese un numero positivo: "))
        if n > 0:
            return n  
        print("El número debe ser mayor que 0. Inténtalo de nuevo.") 

def calcular_tabla(n):
    for i in range(1, 11):
        print(n, "X", i, "=", n * i) 
while True:
    n = pedir_numero() 

    calcular_tabla(n)
    
    continuar = int(input("Si no desea continuar pulse 0: "))
    if continuar == 0:
        print("¡Hasta luego!")
        break