class Coche():

	def desplazamiento(self):
		print("Me desplazo con 4 ruedas")


class Moto():

	def desplazamiento(self):
		print("Se desplaza con 2 ruedas")

class Camion():

	def desplazamiento(self):
		print("Me desplaza utilizando 6 ruedas")

#miVehiculo=Moto()

#miVehiculo.desplazamiento() 

#miVehiculo2=Coche()

#miVehiculo2.desplazamiento()

#miVehiculo3=Camion()

#miVehiculo3.desplazamiento() 

def desplazamientovehiculo(vehiculo):         #esto es un método, "vehiculo" un objeto
	vehiculo.desplazamiento()

#el obnjeto puedo cambiar de forma gracias al polimorfismo:


miVehiculo4=Moto()

desplazamientovehiculo(miVehiculo4)


