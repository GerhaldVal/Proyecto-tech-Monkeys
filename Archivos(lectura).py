with open ('Menu_Creado_con_archivo,write','r', encoding = 'utf-8') as archivo: # Esto sirve para abrir y cerrar el archivo directamente despues de usarlo, encoding "utf-8" ayuda a que python no tenga problemas al leer el archivo
    contenido = archivo.read()
    print(contenido)
opcion=int(input("eliga una opcion \n "))
match opcion:
    case 1:
        print("gracias por elegir")
    case 2:
        print("gracias por elegir")
    case 3:
        print("gracias por elegir")
    case 4:
        print("gracias por elegir")
    case 5:
        print("gracias por elegir")
print("salio del menu")

    
    
