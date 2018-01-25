"""  Bucles """
listaMascotas=[ "Pelusa","Mechis","Lulu",True,False,5.4,2 ]

for i in ["Pelusa","Tomas","Tomasa"]: # Itera segun la cantidad de elementos de la lista.
    print("Mascotas") # i, toma el valor de cada elemento de la lista.




for i in "gorsitho@gmail.com": # Itera segun la cantidad de la letras del string.
    print(i,end=' - ') # Al final de cada print ira - sin saltar de linea.

    email=True if i=='@' else False # Operador ternario en Python.
    if email:
        print("")
        print(f"Email es verdadero por que tiene un {i}") # Notacion especial, funcion de tipo f, concatena con la variable que esta entre corchetes.
print("")
for i in range(4,8,2): # Itera desde el 4 hasta el 8 en dos en dos 
    
    print("******"+str(i))

print("")
for i in range(len(listaMascotas)): # Recorre segun la longitud de la lista.
    
    print(str(listaMascotas[i])+""+str(i))
else:
    
    print("Termino el ciclo for para el listado de mascotas") # El else usado en un ciclo for se inicia cuando el ciclo haya acabado.


"""While """

iteraciones=0

while iteraciones<10:
    if iteraciones==5:
        iteraciones+=1
        continue #Continua con la siguiente iteracion ignorando lo que sigue del codigo.
    print("***** Ciclo while - "+str(iteraciones))
    
    iteraciones+=1

    
"""------------Despedida ----------------"""
mensajeDespedida=input("Escribe un mensaje de despedida")

