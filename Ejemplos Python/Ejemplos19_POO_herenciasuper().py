class Persona():
	def __init__(self, nombre, edad, residencia):


		self.nombre=nombre
		self.edad=edad
		self.residencia=residencia

	def descripcion(self):

		print("Nombre: ", self.nombre, "edad: ", self.edad, "Residencia en: ", self.residencia)


class Empleado(Persona):

	def __init__(self, salario,antiguedad,nombre_empleado,edad_empleado,residencia_empleado):

		super().__init__(nombre_empleado,edad_empleado,residencia_empleado) #Lo Pasamos al constructor init de la clase paDre

		self.salario=salario

		self.antiguedad=antiguedad

	def descripcion(self):

		super().descripcion()

		print("Salario: ", self.salario,"Antiguedad: ",self.antiguedad)

Arturo=Empleado(1500,156,"Arturo", 56, "madrid")

Arturo.descripcion()

print(isinstance(Arturo,Persona))

Manuel=Persona("Manuel",19,"Alicante")

Manuel.descripcion()

print(isinstance(Manuel, Empleado))
