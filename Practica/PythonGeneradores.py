
""" Generadores 
-Estructuras que extraen valores de una funcion y se almacenan en objetos iterables.
- Se almacena en uno en uno
- Cuando se almacena un valor, este se pausa hasta que se solicite el siguiente.(Suspension de estado).

"""

def generadorPares(limite): 
    num=0
    while num<limite:
        yield num*2 
        num+=1

devuelvePares=generadorPares(10)

print("***")

print(next(devuelvePares))

print("***")

print(next(devuelvePares))

print("***")

print(next(devuelvePares))

print("***")
   
def devuelveApellidos(*apellidos):# El parentisis indica un numero indeterminado de argumentos, es decir, es dinamico. Los recibe en forma de Tupla.

    
    for elemento in apellidos:
        
        yield from elemento # yield from, simplifica la sintaxis de un bucle for anidado.



apellidosDevueltos= devuelveApellidos("Velasquez","Angarita","Rodriguez")
print("***")

print(next(apellidosDevueltos))

print("***")

print(next(apellidosDevueltos))

print("***")



"""------------Despedida ----------------"""
mensajeDespedida=input("Escribe un mensaje de despedida")
