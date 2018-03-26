def evaluaedad(edad):

	if edad<0:
		raise TypeError("No se permiten edaders negativas")

	if edad<18:
		return "Eres menor"
	elif 18<edad<60:
		return("eres adulto")
	elif 60<edad<100:
		return("eres anciano")
	elif edad>100:
		return ("estás en la ultima vuelta del camino")

print(evaluaedad(5))


print("__________Ejemplo2________")


import math

def calcularaizcuadrada(num):

	if num<0:
		raise ValueError ("El numero no puede ser negativo")
	else:
		return math.sqrt(num)

Opp=int(input("Introduce numero: "))

try:
	print(calcularaizcuadrada(Opp))

except ValueError as ErrorNumeroNegativo:
	print(ErrorNumeroNegativo)

finally:
	print("FIN")
