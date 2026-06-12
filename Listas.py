cantdad=int(input("Cantidad de usuarios "))
listado=[]
for i in range(1,cantdad+1):
    a=input("Nombre del cuenta ")
    b=input("Tipo de cuenta ")
    c=input("Contraseña ")
    lista={"Nombre de la cuenta": a , "Tipo de cuenta": b ,"Contraseña":c}
    listado.append(lista)

print(listado)
