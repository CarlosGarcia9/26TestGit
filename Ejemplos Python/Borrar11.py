class coche():

	def __init__(self):
		self.largo=25
		self.ancho=12
		self.enmarcha=False
		self.gasolina=False

	def gasolinera(self):
		self.gasolina=True

	def arrancar(self):
		self.enmarcha=True

	def situacion(self):
		print("Anchura es ",self.ancho," esta en marcha ",self.enmarcha," tiene gasolina ",self.gasolina)

coche1=coche()

coche1.arrancar()

coche1.situacion()

coche2=coche()
coche2.arrancar()
coche2.gasolinera()