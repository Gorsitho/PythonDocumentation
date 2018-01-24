
#PRIMEROS PASOS CON PYTHON, PRACTICANDO SU SINTAXIS


#Este es un comentario de una linea.

""" Este es un comentario 
multilinea
asdasd"""

import math # De esta manera se importa en Prython.

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

"""Control de flujo 

- No existe el Switch
- Concatenacion de operadores logicos.
"""


#Sintaxis de un control de flujo, condicional.

numeroFlujo=15

if 0<numeroFlujo<16: 
    print("El numero "+ str(numeroFlujo)+" esta entre los rangos 0 y 16")
    

elif numeroFlujo<=0:
       print("El numero "+ str(numeroFlujo) + " es negativo ")  
else :
    
    print("El numero "+ str(numeroFlujo) + " no esta entre el rango.")


generoPersona="MaScUlino".lower();

if generoPersona in ("masculino","femenino"):

    print("El genero es correcto")

else:
    print("Genero incorrecto")

edadMascota1=4
nombreMascota=""    

#and,or,not
if 100>edadMascota1>0 and nombreMascota!="":
    
    print("Tu mascota llamada "+nombreMascota+" tiene una edad de "+str(edadMascota1))
else:
    print(" Error, la edad o el nombre de la mascota es invalido")

"""  Bucles """


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



if apellidosDevueltos=="":
    
    raise TypeError("Ocurrio un error en la tupla de apellidosDevueltos") #Lanza una excepcion escogiendo su tipo:ZeroDivisionError,ValueError,etc... bajo una condicion.



""" POO  """
class PersonajeClan():
    def __init__(self,clan,descripcion):
        self.__nombreClan=clan
        self.__descripcionClan=descripcion
    
    def descripcion(self):
        print("El nombre del clan es :",self.__nombreClan," y su descripcion es", self.__descripcionClan)

#Nomenclatura del punto: Forma para ingresar a cualquier metodo de algun objeto.
class Personaje():
    def __init__(self): #Constructor.
        # Se les debe agregar self para que se puedan identificar como variables de la clase.
        self.__nombrePersonaje="Daniel"
        self.__ataquePersonaje=15 #Encapsulamiento, se realiza con dos rayapiso.
        self.__defensaPersonaje=20 # Solo accesible desde la propia clase.
        self.__nivel=10
        self.__experiencia=0

    def subirNivel(self): # El self es similar al this, sin embargo, se obliga a utilizarlo siempre.
        self.__nivel+=1  # Personaje().nivel+=1, el self llama a la misma clase.
         

    def estadoPersonaje(self, mensaje): # luego del self van los argumentos que se quieren agregar.
        self.__obtenerExp() 
        if self.__nivel!=10:
            return "Subio de nivel - "+mensaje+" y su experencia esta en "+str(self.__experiencia)
        else:
            return "No subio de nivel"

    def __obtenerExp(self): # Metodo encapsulado.
        self.__experiencia+=10
        return "Subio su experiencia"

""" Herencia
- Python si admite la herencia multiple.
"""
class PersonajeArquero(PersonajeClan,Personaje): # De esta manera se hereda, la herencia tiene prioridad en el primero heredando su constructor.

    def __init__(self,clan,descripcion):
        super().__init__(clan,descripcion) # Se instancia el constructor heredado con mas prioridad.
        self.__nombrePersonaje="Daniel"
        self.__ataquePersonaje=15 
        self.__defensaPersonaje=20 
        self.__nivel=10
        self.__experiencia=0


    def estadoPersonaje(self, mensaje): # luego del self van los argumentos que se quieren agregar.
        return "El arqueri subio de nivel - "+mensaje+" y su experencia esta en "+str(self.__experiencia)
    def descripcion(self):
        super().descripcion()  # Se instancia el metodo de la clase Padre, proveniente de su herencia.
        print("El nombre del personaje es :",self.__nombrePersonaje," y su nivel es de ", self.__nivel)

miPersonaje= Personaje()
miPersonaje.subirNivel()

print(str(miPersonaje.estadoPersonaje("Gracias por su atencion, lalaalla")))


miArquero= PersonajeArquero("Los pikachus"," Es un clan en el que se crian pokemones de tipo pikachu. LOL xd")
print(str(miArquero.estadoPersonaje("Gracias por su atencion, lalaalla")))
print(str(miArquero.descripcion()))


# Principio de sustitucion: Siempre es uno(a), ejemplo: Un arquero siempre es un personaje, un personaje no siempre es un arquerp.

print(isinstance(miArquero,Personaje)) # Devuelve True si el objeto miArquero es de la clase Personaje, lo cual lo es por que su clase hereda de Personaje.



""" Modularizar - Paquetes
"""

# import nombreArchivo  # De esta manera se importa, sin embargo se tendria que usar la nomenclatura del punto si se hace asi.

# from nombreArchivo import funcionclase # Importa una funcion especifica o una clase especifica.
# from nombreArchivo import *   # Importa todos los metodos, no hay necesidad de usar la nomenclatura del punto.

# Se puede instanciar cualquier clase que este dentro del archivo importado.

# Para crear un paquete, se debe crear un carpeta normal. Sin embargo, dentro de la 
# carpeta se almacenara un archivo llamado "__init__.py", de esta manera python reconocera la carpeta como paquete.

#from nombrePaquete.nombreArchivo import nombreClase # De esta manera se importa un paquete.

#from nombrePaquete.nombreSubPaquete.nombreArchivo import nombreClase # De esta manera se llama un archivo en un subpaquete.






"""------------Despedida ----------------"""
mensajeDespedida=input("Escribe un mensaje de despedida")

