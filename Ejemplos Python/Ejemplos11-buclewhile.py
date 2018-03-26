i=1

while i<=10:

	print("ejecucion" + str(i))

	i=i+1

print("\t se acabo")


print("______________________bucle2_________________________")

edad=int(input("Introduzca edad:  "))

while edad<5 or edad>100:
	print("Edad incorrecta")
	edad=int(input("Introduzca edad:  "))

print("Puedes pasar")
print("Edad= " , edad, "est" + str(edad))

print("-----------BucleraizCuadrada------------")

import math

numero=int(input("introdzca un numero: "))

intentos=0

while numero<0:
	print("Es negativo!!!")

	if intentos==3:
		print("yA BASTA")
		break;

	numero=int(input("introdzca un numero: "))

	if numero<0:
		intentos=intentos+1

if intentos<3:
	solution=math.sqrt(numero)
	print("La raiz de " + str(numero)+"es "+str(solution))


