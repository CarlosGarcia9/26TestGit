def generador(param):
	num=1

	while num<param:

		yield num**2

		num=num+1

devuelve=(generador(50))

print(next(devuelve))
print(next(devuelve))
print(next(devuelve))
print(next(devuelve))
print(next(devuelve))