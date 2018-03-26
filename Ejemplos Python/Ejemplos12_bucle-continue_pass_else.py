for letra in "Madrid":

	if  letra=="r": #Para saltarse la letra r en el for usamos un continue
		continue

	print(letra)

print("---------------------------2---------------------")

nombre="aprendiendo python"

contador=0

for i in nombre:

	if i==" ":
		continue #para contar el numero de caracteres sin espacio
	contador+=1

print(contador)

print(len(nombre))


print("-----------------pass----------------")

#while True:
#	pass

print("------------pass para crear clase------------")

class Clase:
 	pass # ya lo haremos

print("-----otro----")


email=input("Introduzca mail: ")

for i in email:
	if i=="@":

		 arroba=True


		
	else:
		arroba=False

print(arroba)

