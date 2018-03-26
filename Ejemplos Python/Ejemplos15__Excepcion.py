#Excepciones try: except nombre_del_error:
def suma(num1,num2):
	return num1+num2

def resta(num1,num2):
	return num1-num2

def multiplica(num1,num2):
	return num1*num2

def divide(num1,num2):

	try:
		return num1/num2

	except ZeroDivisionError:
		print("No se puede dividir por 0")
		return "Operacion erronea"

while True:

	try:
		op1=(int(input("Introduzca numero1:  "))) 
		op2=(int(input("Introduzca numero2:  "))) 
		break
	except ValueError:
		print("Debes introducir un entero")

operacion=input("Operación a realizar(suma,resta,divide,multiplica): ")

if operacion=="suma":
	print(suma(op1,op2))
elif operacion=="resta":
	print(resta(op1,op2))
elif operacion=="multiplica":
	print(multiplica(op1,op2))
elif operacion=="divide":
	print(divide(op1,op2))
else:
	print("No se contempla tal operación")

print("Operacion ejecutada")

print("________Ejemplo2_________")
def dividir():

	try:
		option1=(float(input("Introduce numero1:   ")))
		option2=(float(input("Introduce numero2:   ")))

		print("La division es  " + str(option1/option2))

	except ValueError:
		print("El valor no es correcto")

	except ZeroDivisionError:

		print("No puedes dividir por 0")
	finally:
		print("calculo finalizado")

	print("calculo finalizado")

dividir()

