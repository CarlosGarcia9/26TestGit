import pyodbc

con=pyodbc.connect("DRIVER={SQL Server};server=LAPTOP-ET8H5O79;database=Prueba")
cur=con.cursor()
while (True):
	print("""¿que procesamiento desea crear?
		1) Obtener edades mayores a cierta edad
		2) Obtener edades menor a cierta edad
		3) Salir del menu""")
	opcion=int(input("Introduce el proceso que desea realizar: "))
	if opcion==1:
		edad=int(input("Introduce una edad: "))
		cur.execute("exec dbo.seleccion %s"%edad)
		#cur.execute=("exec [Prueba].[dbo].[Prueba](?)",(edad))
		for row in cur:
			print(row.NOMBRE+" "+str(row.EDAD))
	break
