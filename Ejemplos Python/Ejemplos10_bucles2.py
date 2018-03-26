for i in range(5,60,4): #de 5 a 60 de 4 en 4
	print(f"valor de la variable {i} .txt") # las llaves concatena la variable al texto, si no ponemos la f no entiende e imprime  de forma literal

print("-----------------Segundo Bucle-----------")

valido=False

email=input("Introduce email ")
for j in range(len(email)):
	if email[j]=="@":  #posicion en un texto []

		valido=True

if valido==True:
	print("Bien")

else:
	print("Nooooooooooooooooo!")
