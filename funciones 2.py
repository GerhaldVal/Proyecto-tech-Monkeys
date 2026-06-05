def menor(a,b):
    if a < b:
        return a
    else:
        return b
    
def pedir_numero(mensaje):
    while True:
        N = int(input(mensaje))
        if N > 0:
            return N

N = pedir_numero("ingrese la cantidad de veces")
        
for i in range(N):
    print(f"{i+1} de {N}")
            
    a = pedir_numero("ingrese un numero")
    b = pedir_numero("ingrese otro numero")
        
    c = menor(a, b)
        
    print(f"el valor de {c} es menor")