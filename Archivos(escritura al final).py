with open ("prueba_de_archivo_2.txt","a", encoding = "utf-8" ) as archivo: # aqui utilizamos el comando "a" (at end) para escribir archivos al final del texto sin sobreescribir el antiguo archivo
        archivo.write ("esta linea se añade al final del archivo gracias al comando with open , a \n")
