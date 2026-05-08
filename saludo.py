
numero1=int(input("Ingrese un numero"))
numero2=int(input("Ingrese  otro numero"))
print("""MENU:
      1) SUMAR 
      2) RESTAR
      3) MULTIPLICAR
      4) DIVIDIR
      5) SALIR""")
lol=int(input("Que opcion quieres?"))
while lol !=5 :
    match lol:
      case 1:
            total=numer1+numero2
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
   lol=int(input("Que opcion quieres?"))
              
            
            
