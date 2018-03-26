import sys
from pymongo import MongoClient

client = MongoClient('localhost', 6000)

#Conexion a base de datos azul
db = client.Azul

#Insertar una coleccion en MongoDB
db.sites.insert({"url":"http://www.algo.com", "name":"Carlos"})

###Leer un coleccion,creamos una variable y guardamos ahí los documentos
site =db.sites.find_one()

#Imprimimos site
print(site)

#Es como un diccionario por lo que podemos sacar un valor de una clave
print(site["name"])

#Meto dinamico
print("Me gusta %s y la url es %s" %(site["name"],site["url"]))

site2=db.sites.find()

print(site2)

for s in site2:
	print(s["name"])



