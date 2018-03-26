class coche():
	def __init__(self,marca,modelo):
		self.tamaño=1236
		self.marca=marca
		self.modelo=modelo

	def reduccion_tamaño(self):
		self.tamaño=4

Coche1=coche("Mercedes","Benz")

Coche1.reduccion_tamaño()

print(self.marca)