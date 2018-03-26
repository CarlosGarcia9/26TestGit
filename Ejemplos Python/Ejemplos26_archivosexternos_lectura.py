from io import open

#archivo_texto=open("archivo.txt","r")

#texto=archivo_texto.read() #que lea lo que hay en ese archivo y lo amacene en la variable texto

#lineas_texto=archivo_texto.readlines() #almacena en una lista

#archivo_texto.close()

#print(lineas_texto[0])

#agregar lineas de texto
#archivo_texto=open("archivo.txt", "a")  # a de append

#archivo_texto.write("\n siempre es una buena ocasion para estudiar python")

#archivo_texto.close()

archivo_texto=open("archivo.txt", "r+") #r+ de lectura y escritura
#print(archivo_texto.read())


#archivo_texto.seek(0) # seek: dónde poner la posición del cursor
#si ponemos archivo_texto.seek(10) empieza a escribir en la pos. 10
#print(archivo_texto.read(15)) # lee hasta el 15

#print(archivo_texto.readlines())

lista_texto=archivo_texto.readlines();


lista_texto[1]="Esta línea ha sido incluida\n "

archivo_texto.seek(0)



archivo_texto.writelines(lista_texto)


archivo_texto.close()











