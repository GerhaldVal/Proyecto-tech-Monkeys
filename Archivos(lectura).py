with open ('ejemplo.txt','r', encoding = 'utf-8') as archivo: # Esto sirve para abrir y cerrar el archivo directamente despues de usarlo, encoding "utf-8" ayuda a que python no tenga problemas al leer el archivo
    contenido = archivo.read()
    print(contenido)