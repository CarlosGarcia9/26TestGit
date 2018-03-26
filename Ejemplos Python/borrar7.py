email=input("Introduzca email:")

Verdadero=False

for i in range(len(email)):
	if email[i]== "@":

		Verdadero=True

if Verdadero==True:

	print("Todo correcto")

else: 

	print("No esta bien")


