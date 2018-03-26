def generador(limite):

	num=1

	lista=[]

	while num < limite:
		
		lista.append(2*num)

		num = num +1


	return lista

print(generador(23))