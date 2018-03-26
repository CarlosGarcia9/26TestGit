diccionario={"Alemania":"Berlin", "Italia":"Roma", "España":"Madrid", "Rusia":"Moscu"}

print(diccionario["Alemania"]) #buscamos por clave

diccionario["Irlanda"]="Dublin" #añadimos un elemneto

print(diccionario)

del diccionario["Alemania"] #eliminamos por clave

print(diccionario)


diccionario[23]="Jordan" 

print(diccionario)


Lista=["China","Japon","Indonesia"]

diccionario2={Lista[0]:"Pekin",Lista[1]:"Tokio",Lista[2]:"Yakarta"}
print(diccionario2)

diccionario3={"Nombre":"Michael", "Apellido":"Jordan", "Numero":23, "Anillos":[91,92,93,96,97,98]}

print(diccionario3)


diccionario4={"Nombre":"Michael", "Apellido":"Jordan", "Numero":23, "Anillos":{"temporadas":[91,92,93,96,97,98]}} #diccionario dentro de un diicionario
print(diccionario4.keys()) 
print(diccionario4.values())
print(len(diccionario4))
print(diccionario4)



