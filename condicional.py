print("Notas y promedio")
nota1=float(input("Ingrese la primera nota"))
nota2=float(input("Ingrese la segunda nota"))
nota3=float(input("Ingrese la tercera nota"))

Promedio=(nota1+nota2+nota3)/3

if Promedio<4.0:
    print("Reprobaste la materia con un proemdio",Promedio)
elif Promedio>=4.0:
    if Promedio==7.0:
        print("Aprobaste de foma perfecta con promedio ",Promedio)
    else:
        print("Aprobaste con promedio",Promedio)
