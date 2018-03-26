#Qué son los generadores? Extraen objetos de un función y se almacenan en objetos iterables, se almacenan uno a uno y el generedaor se mantiene pausado hasta que se solicita el siguientye elemento
#En funcion:   def generanumertos()
					#return numeros         conbstruye toda la lista

#En generador  def generanumertos()
					#yield numeros 			construye objeto iterable, cada vez que llamamos al generedaor saca un elemento         

#ventajas: eficiencia, utiles para listas infinitas ....

print("_________GEnera Pares Utilizando funcion_________")

def generapares(limite):
	num=1

	lista=[]

	while num<limite:

		lista.append(num*2)

		num=num+1

	return lista

print(generapares(15))


print("_________GEnera Pares Utilizando generador_________")

def generapares2(limitee):
	nume=1

	while nume<limitee:

		yield nume*2

		nume=nume+1

devuelvepares=(generapares2(15))

for i in devuelvepares:
	print(i)

print("_________GEnera Pares Utilizando generador,uno a uno Next_________")

def generapares3(limiteeee):
	numer=1

	while numer<limiteeee:

		yield numer*2

		numer=numer+1

devuelvepares2=(generapares3(15)) 

print(next(devuelvepares2)) #printea el primero

print("aquí podría haber más código")

print(next(devuelvepares2)) #printea el siguiente

print("aquí podría haber más código")

print(next(devuelvepares2)) #continua printeando

print("aquí podría haber más código")







