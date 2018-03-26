#Persistendia de datos: archivos externos o en BBDD
#Archivos externois, 4 fases: Creación, apertura, manipulación y cierre.
#Usaremos módulo io de la biblioteca estaándar


from io import open

archivo_texto=open("archivo.txt","w")  # primer argumento elprint(next(paises_devueltos)) path: "c:\\............txt"  

frase="Estupendo día para invadir Polonia \n cuando escucho Wagner"


archivo_texto.write(frase)

archivo_texto.close()