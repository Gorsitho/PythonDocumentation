"""Excepciones
- Errores en tiempo de ejecucion o logicos, Errores de compilacion

"""

try:
    variable=0/0
    print("Codigo...") #Bloque de instrucciones vulnerable a excepciones.
except ZeroDivisionError as ErrorZero:# as Sirve para dar un alias a la excepcion, es un objeto.
    print("Error, division por cero.",ErrorZero) #Bloque de instrucciones en caso que sufra una excepcion del tipo ZeroDivisionError.
except ValueError: 
    print("Codigo...") # Pueden concatenar mas de una excepcion.
except:
    print("Codigo..") # Error en general. Captura cualquier tipo error.
    
finally: # Siempre se ejecuta lo que hay en el bloque de finally.
    print("Mensaje final")  

apellidosDevueltos="lala    "

if apellidosDevueltos=="":
    
    raise TypeError("Ocurrio un error en la tupla de apellidosDevueltos") #Lanza una excepcion escogiendo su tipo:ZeroDivisionError,ValueError,etc... bajo una condicion.


"""------------Despedida ----------------"""
mensajeDespedida=input("Escribe un mensaje de despedida")

