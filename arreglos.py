pisos = [1,2,3,4,5]
while True:
    print("Pisos:",pisos)
    piso = int(input("Ingrese el piso al que desea llegar\n"))
    if 1<= piso <= 5 :
        break
    print("Piso invalido (Ingrese un piso del 1 al 5)")
print("Usted ha llegado al piso:",piso)
