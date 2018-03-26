#programa cumple requisitos beca mas de 40km distancia, sdalario<20000, numero de hermanos > 3

print("Programa de becas")

distancia_colegio=int(input("Introduce la distanmcia: "))

print(distancia_colegio)

numero_hermanos=int(input("Introduce numero de hermanos: "))
print(numero_hermanos)

salario_familiar=int(input("Introduce Salario: "))
print(salario_familiar)

if distancia_colegio>40 and numero_hermanos >=3 and salario_familiar<20000:
	print("mereces una beca")
else:
	print("No tienes derecho a beca")
print("---------------------------------0tra------------------------")


print("Deportes:Futbol, Tenis, Padel")
Deporte_optativo=input(("Intruzca el deporte optativo:  "))

if Deporte_optativo in ("Futbol", "Tenis", "Padel"):
	print("has escogido: " + Deporte_optativo)

else:
 	print("deporte no existente")
