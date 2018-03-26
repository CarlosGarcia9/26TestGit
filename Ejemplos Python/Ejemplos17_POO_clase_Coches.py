class Coche():

	def __init__(self):     #construimos un constructor de la clase(estado inicial)

		self.__largoChasis=250
		self.__anchoChasis=60
		self.__ruedas=4
		self.__Enmarcha=False    #Están son las propiedades,estado inicial lo especificamos con un constructor.

		# para encapsular __ antes de las  metodos
	def arrancar(self,arrancamos):    #esto es un método
		
		self.__Enmarcha=arrancamos

		if(self.__Enmarcha):
			 chequeo=self.__chequeointerno()

		if (self.__Enmarcha and chequeo): #esto es otro método
			return "El coche está arrancado"

		elif(self.__Enmarcha and chequeo==False):
			return "Algo ha ido mal"

		else:
			return("El coche NO está arrancado")


	def estado(self):

		print("El coche tiene", self.__ruedas, "ruedas. ", " Un ancho de", self.__anchoChasis, "y un largo de", self.__largoChasis)

	
	def __chequeointerno(self):
		print("Realizando chequeo interno ")

		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):

			return True

		else:

			return False


miCoche=Coche()  #Instanciar una clase

print(miCoche.arrancar(True)) #Si queremos cambiar el comportamienbto, el metodo, arrancar miCoche

miCoche.estado()

print(miCoche.__chequeointerno()) #No podemos cambiarlo desde fuera, por lo que da error

print("--- A continuacion creamos un segundo objeto ---")

miCoche2=Coche()

print(miCoche2.arrancar(False))

miCoche2.__ruedas=2   # No modifica nada porque ruedas está encapsulada con __ antes de ruedas: __ruedad. La variable ruedas no está accesible desde fuera de la clase.

miCoche2.estado ()

print(miCoche2.__chequeointerno()) #No podemos cambiarlo desde fuera, por lo que da un error





