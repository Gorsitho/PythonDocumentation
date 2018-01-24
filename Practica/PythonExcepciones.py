"""Excepciones
- Errores en tiempo de ejecucion o logicos, Errores de compilacion

"""

try:
    print("Codigo...") #Bloque de instrucciones vulnerable a excepciones.
except ZeroDivisionError:
    print("Codigo...") #Bloque de instrucciones en caso que sufra una excepcion del tipo ZeroDivisionError.
except ValueError as ErrorenelValor: # as Sirve para dar un alias a la excepcion, es un objeto.
    print("Codigo...") # Pueden concatenar mas de una excepcion.
except:
    print("Codigo..") # Error en general.
    
finally: # Siempre se ejecuta lo que hay en el bloque de finally.
    print("Mensaje final")  

apellidosDevueltos="lala    "

if apellidosDevueltos=="":
    
    raise TypeError("Ocurrio un error en la tupla de apellidosDevueltos") #Lanza una excepcion escogiendo su tipo:ZeroDivisionError,ValueError,etc... bajo una condicion.


"""------------Despedida ----------------"""
mensajeDespedida=input("Escribe un mensaje de despedida")

