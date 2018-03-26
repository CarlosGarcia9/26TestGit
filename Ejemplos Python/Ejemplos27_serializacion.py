#Serialización: guardar en un fichero externo (una coleecion, un diiccionario un objeto)
#con la particularidad de almacenado en codigo binario
#Necesidad: distribuir por internet, o si queremos almacenar en externo o para almacenar en una BBDD
#Usaremos la biblioteca pikl()
#  dump()       volcado de datos al fichero binario externo
#  load()       carga de los datos del fichero binario externo

import pickle

lista_nombres=["Pedro","Alfonso","Ana","Isabel"]

fichero_binario=open("lista_nombres","wb") # wb escritura binaria

pickle.dump(lista_nombres, fichero_binario) #1 que queremos volar, 2 en donde

fichero_binario.close()

del(fichero_binario)