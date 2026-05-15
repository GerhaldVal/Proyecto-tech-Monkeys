while True:
    # Bucle para asegurar que el número sea positivo
    while True:
        n = int(input("Ingrese un numero positivo: "))
        if n > 0:
            break
        print("El número debe ser mayor que 0. Inténtalo de nuevo.") 
    # Usamos range(1, 11) para ir del 1 al 10
    for i in range(1, 11):
        print(n, "X", i, "=", n * i)     
    # Preguntar al usuario si desea continuar
    continuar = int(input("Si no desea continuar pulse 0: "))
    if continuar == 0:
        print("¡Hasta luego!")
        break
