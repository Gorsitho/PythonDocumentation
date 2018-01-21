
#PRIMEROS PASOS CON PYTHON, PRACTICANDO SU SINTAXIS


#Este es un comentario de una linea.

""" Este es un comentario 
multilinea
asdasd
"""



def mensaje():

    print("Esta es una instruccion")
    print("Esta es una instruccion")
    print("Esta es una instruccion")
    print("Esta es una instruccion")

# En python no es necesario especificar el tipo de variable.
numero1=5
numero2=3

#Tipos de funciones.

def suma(num1,num2):    
 
    return num1+num2  

mensaje() #Utilizando el metodo metodo.

print( suma(numero1,numero2)) # Imprimir en consola.

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


#Sintaxis de un control de flujo, condicional.

if numero1>numero2: 
    print("La variable numero1 es mayor ")
    
else :
    
    print("La variale numero2 es mayor")



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



