tupla=("carlos", 11,12,2017)

lista=list(tupla) #paso una tupla a lista

print(lista)

lista2=["pepe",2,3,3] 

tupla2=tuple(lista2) #paso una lista a tupla

print(tupla2)

print("pepe" in tupla2)

print(tupla[3])

print(tupla2.count(3)) #cuenta cuantos 3's hay in mi tupla

print(len(tupla2))

tuplaunitaria=("Carlos",)
print(len(tuplaunitaria))

name, day, month, year = tupla #asigno un nombre a cada campo de la tupla definida anteriormente


print(name)
print(day)
print(month)
print(year)

