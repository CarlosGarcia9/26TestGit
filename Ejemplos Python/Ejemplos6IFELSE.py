print("verificacion de acceso")

edad_usuario=int(input("Introduzca su edad"))

if edad_usuario<18:
	print("No puedes pasar!")
elif edad_usuario>120:
	print("demasiado mayor")

else:
	print("Puedes pasar")

print("FIN")
