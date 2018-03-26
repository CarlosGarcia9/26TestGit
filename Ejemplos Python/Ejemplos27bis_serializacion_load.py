import pickle

fichero=open("lista_nombres","rb") #rb read binary

lista=pickle.load(fichero) #carga la lista

print(lista)