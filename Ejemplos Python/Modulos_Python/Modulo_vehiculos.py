class vehiculos:

	def __init__(self,marca,modelo):

		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		
		self.enmarcha=True

	def acelerar(self):

		self.acelera=True

	def frenar(self):

		self.frena=True

	def estado(self):

		print("Marca: ", self.marca, "\nModelo: ", self.modelo,"\nEn marcha: ", self.enmarcha, "\nAcelera: ", self.acelera, "\nFrena: ", self.frena)


class moto(vehiculos):                         #creamos la clase moto que hereda de la clase vehiculos
	imotoloop="No hago loop"
	def motoloop(self):
		self.imotoloop="hago un loop con la moto"
	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo,"\nEn marcha: ", self.enmarcha, "\nAcelera: ", self.acelera, "\nFrena: ", self.frena,"\n", self.imotoloop)

class furgoneta(vehiculos):

	def carga(self,cargar):
		self.cargado=cargar
		if(self.cargado==True):
			return "la furgoneta está cargada"
		else:
			return "la furgoneta está sin cargar, vacía"

class Veco(vehiculos):

	def __init__(self,marca,modelo):

		super().__init__(marca, modelo)
			
		self.autonomia=100


	def cargar_energia(self):

			self.cargando=True

