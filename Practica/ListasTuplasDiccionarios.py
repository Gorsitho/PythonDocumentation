
"""Listas

-Se pueden utilizar los operadores matematicos en ella 
-Se pueden agregar, eliminar, mirar cualquier objeto.
-Admite cualquier tipo de valor en ellas.
"""

listaMascotas=[ "Pelusa","Mechis","Lulu",True,False,5.4,2 ]*2 

listaMascotas.append("Juanchito") #Agrega un nuevo objeto al final de la lista.

listaMascotas.insert(2,"Tomas") #Agrega el objeto en la posicion deseada.

listaMascotas.extend(["lalala,lolololo"]) # Se extiende la lista con nuevos objetos.

listaMascotas.remove("Mechis") #Remueve el objeto de la lista.

listaMascotas.pop() #Elimina el ultimo objeto de la lista.

print(listaMascotas.index("Tomas")) #Nos da el indice del objeto en la lista.

print(listaMascotas[:]) #Imprime todo el objeto lista.

print(listaMascotas[1:3]) #Imprime entre los rangos de indice 1 y 3.

print(listaMascotas[2]) #Imprime el objeto del indice 2

print(listaMascotas[-2]) #Muestra el segundo objeto de izquierda a derecha, sin empezar desde 0.

print("Daniel" in listaMascotas) #Comrpueba si el objeto esta en la lista





""" LAS TUPLAS

- Son inmutables, es decir que no cambian durante la ejecuacion.
- Si permite extraer una porcion de la tupla, sin embargo, crea una nueva tupla.
- Si permite comprobar un objeto.
- Mas rapidas.
-Menor espacio.
- Pueden utilizarse como claves en un diccionario.
- nombreTupla=(n1,n2,n3)  <- los parentesis son opcionales.
 """

miTupla=("Daniel","Natalia")
milista=list(miTupla) # Convierta la tupla en lista. tuple() <- de lista a tupla.

novio,novia=miTupla#Desempaquetado de Tuplas

print(novio) # Imprime el valor de la variable.
print(novia) 
print(miTupla.count("Daniel")) #Cuantas veces aparece ese objeto.

print(len(miTupla)) # Length en Python



"""Diccionarios 

- Estructura de datos.
- Se asocian clave:valor.
- No estan ordenados.
- No pueden existir dos claves con el mismo nombre, se remplezan siendo asi.

"""
# Los diccionarios pueden tener diccionarios,tuplas, listas, etc. Dentro de ellos.
midiccionario={"Colombia":"Bogota","Mexico":"CDMexico","One piece":("Luffy","Zoro","Nami")}
midiccionario["España"]="Madrid" # Se agrega el objeto si no existe, si no, lo remplaza.
del midiccionario["Mexico"]
#diccionarioTupla={miTupla(0):"jeje",miTupla(1):"jojojo"}


#print(diccionarioTupla)
print(midiccionario.keys()) # Todas las claves del diccionario
print(midiccionario.values()) # Todas los valores del diccionario
print(midiccionario)
print(midiccionario["Colombia"]) # Muestra el valor de la clave Colombia


numeroIngresar=input("Introduce un numero ")

print(int(numeroIngresar))



"""------------Despedida ----------------"""
mensajeDespedida=input("Escribe un mensaje de despedida")
