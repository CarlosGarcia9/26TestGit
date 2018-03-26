email=input("Introduzca email:")

contador=0
for j in email:
	if j=="." or j=="@":
		contador=contador+1

if contador==2:
	print("parece correcto")

else:
	print("algo falla,hulio")



