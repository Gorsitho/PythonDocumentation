
""" Generadores 
-Estructuras que extraen valores de una funcion y se almacenan en objetos iterables.
- Se almacena en uno en uno
- Cuando se almacena un valor, este se pausa hasta que se solicite el siguiente.(Suspension de estado).
- Son mas rapidas, ya que no crea el espacio de memoria completo al solicitar alguna accion con ese objeto, solo el necesario espacio.
"""

def generadorPares(limite): 
    num=0
    while num<limite:
        yield num*2 # Se agrega al yield en cada iteracion.
        num+=1

devuelvePares=generadorPares(10) #ObjetoIterable.

print("***")

print(next(devuelvePares)) #Muestra cada par en uno en uno.

print("***")

print(next(devuelvePares))

print("***")

print(next(devuelvePares))

print("***")
   
def devuelveApellidos(*apellidos):# El parentisis indica un numero indeterminado de argumentos, es decir, es dinamico. Los recibe en forma de Tupla.

    
    for elemento in apellidos:
        
        yield from elemento # yield from, simplifica la sintaxis de un bucle for anidado.


print("-----Apellido------")
apellidosDevueltos= devuelveApellidos("Velasquez","Angarita","Rodriguez") # Ingresa los apellidos convirtiendolo en un objeto yield con dos dimensiones.
print("***")

print(next(apellidosDevueltos)) #Muestra la letra V 

print("***")

print(next(apellidosDevueltos)) # Muestra la letra e

print("***")



"""------------Despedida ----------------"""
mensajeDespedida=input("Escribe un mensaje de despedida")
