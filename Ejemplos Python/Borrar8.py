import math

Numero= int(input("Introduzca numero"))


intentos=0

while Numero < 0:

	print("EL NUMERO HA DE SER MAYOR QUE CERO")

	intentos=intentos + 1

	Numero= int(input("Introduzca numero"))
	if intentos==3:
		print("Ya no tienes mas intentos")

		break;

if Numero >= 0:

	raiz=math.sqrt(Numero)


	print(raiz)

