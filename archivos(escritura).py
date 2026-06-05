with open("Menu_Creado_con_archivo,write).txt", "w", encoding="utf-8" ) as archivo: #aqui utilizamos el comando "w" (write) para crear y escribir un archivo con las lineas puestas en el comando
    archivo.write ("################################## \n")
    archivo.write ("########### Menu ################# \n")
    archivo.write ("########### Opcion 1 ############# \n")
    archivo.write ("########### Opcion 2 ############# \n")
    archivo.write ("########### Opcion 3 ############# \n")
    archivo.write ("########### Opcion 4 ############# \n")  # lo dejamos abierto en caso de querer añadir mas opcines "con with open , a"
   