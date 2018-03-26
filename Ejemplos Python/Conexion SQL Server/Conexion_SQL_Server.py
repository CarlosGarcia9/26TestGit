import pyodbc

con = pyodbc.connect("DRIVER={SQL Server};server=DESKTOP-9H7HNL1;database=EjercicioQGIS")
cur = con.cursor()
cur.execute("SELECT * FROM  dbo.Table1")

for row in cur:
	print (row.address + {","} + row[1])

cur.close()
con.close()