print("Empezamos")
nota_del_alumno=input("Introduzca su nota:")

def calificacion(nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspendido"
	return valoracion

print(calificacion(int(nota_del_alumno)))