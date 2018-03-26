class coche ():

	def tipo(self,modelo,marca):

		self.modelo=modelo
		self.marca=marca
		self.altura=1234
		self.limpio=True
	def barro(self):

	 	self.limpio=False
	def caracteristicas(self):
		print("Es un ", self.modelo," ", self.marca, "con un tamaño de ", self.altura, " y esta limpio", self.limpio )


coche_nuevo=coche()
coche_nuevo.tipo("Ferrari","Testa rosa")
coche_nuevo.barro()
coche_nuevo.caracteristicas()
