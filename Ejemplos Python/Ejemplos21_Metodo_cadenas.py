#Al ser python 100% orientado a objetos trata a las cadena de caracteres objetos, objetos string

# Metodos: upper() lower() capitalize() count()  find()
# find() posicion de un caracter/grupo de caracteres ern un texto

# isdigit() numerico isalum() alfanumerico isalpaha()  es letras

# split() dividir palabras utilasndo espacios

# strip() borra espacios sobrantes

# replace() cambia una palabra/letra por otra

# rfind() represente el indice de una letrra contando desde atras

nombreUsuario=input("Introde tu nombre de usuario:  ")

print(" El nombre es:", nombreUsuario.upper())

edad=input("introduzca edad: ")

while (edad.isdigit()==False):

	print("Por favor:introduzca valor numerico")

	edad=input("introduzca edad: ")

if (int(edad)<18):

	print("No puedes pasar")

else:
	print("pasa")