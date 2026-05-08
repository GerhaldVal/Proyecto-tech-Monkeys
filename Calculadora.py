opcion=0
#while para usar un bucle en la calculadora so la opcion no es 5 sige 
while opcion !=5 :
    print("""MENU:
        1) SUMAR 
        2) RESTAR
        3) MULTIPLICAR
        4) DIVIDIR
        5) SALIR""")
    opcion=int(input("Que opcion quieres?"))
    numero1=int(input("Ingrese un numero"))
    numero2=int(input("Ingrese  otro numero"))
#el match es como un swich los casos del menu
    match opcion:
            case 1:
                total=numero1+numero2
                print("El resultado final es",total)
            case 2:
                total=numero1-numero2
                print("El resultado final es",total)
            case 3:
                total=numero1*numero2
                print("El resultado final es",total)
            case 4:
                if numero2!=0:
                    total=numero1/numero2
                    print("El resultado final es",total)
                else:
                    print("no se puede dividir por cero")
print("Te saliste de la calculadora")
                
