def devuelvepaises(*paises):  #numero indeterminado de argumentos en forma de tupla
	for elemento in paises:
		for subelemento in elemento: #Si queremos acceder acceder a los subelementos (las letras de los países)

			yield subelemento

paises_devueltos=devuelvepaises("España","Francia","UK","Portugal")

print(next(paises_devueltos))

print(next(paises_devueltos))

print(next(paises_devueltos))

print(next(paises_devueltos))

print(next(paises_devueltos))


print("__Usando yield from__")


def devuelvepaises(*paises):  #numero indeterminado de argumentos en forma de tupla
	for elemento in paises:

			yield from elemento  #Si queremos acceder acceder a los subelementos (las letras de los países)


paises_devueltos=devuelvepaises("España","Francia","UK","Portugal")

print(next(paises_devueltos))

print(next(paises_devueltos))


