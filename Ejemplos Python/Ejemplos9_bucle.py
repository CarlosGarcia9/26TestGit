for season in ["winter","summer","fall","spring"]:
	print(season)


print("-----------segundobucle--------------")

for i in ["Que",3,"Bye"]:
	print("Hola", end="   ") #end, para decir que hay entre los distintos print


print("\n--------tercer bucle-------------")

contador=0

miemail=input("Introduzca email: ")

for j in miemail:
	if(j=="@" or j== "."):

		contador=contador+1

if contador==2:
	print(" \n email ok")
else:
	print("email wrong")

print("----------------------tiporange---------------")

for k in range(5):
	print(k)





