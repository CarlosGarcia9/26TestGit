lista=["arroz","azucar","pan","naranjas"]

lista.insert(1,"aceite") #dices que posicion
lista.append("sal") # lo mete al final

lista.extend(["berenjenas","tomates", "zanahorias"])

lista.remove("arroz")
	
lista.pop() # quita el ultimo

print(lista[:])


print(lista.index("azucar")) #te dice en que posicion esta azucar

print(lista[2]) #te dice que hay en la posicion 2



print("arroz" in lista) #false o true
print("pepe" in lista) #false o true

lista2=["paco","carlos",2, 3]

lista3=lista+lista2

print(lista3[:])

print(lista[:]*3)




