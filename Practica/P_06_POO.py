
""" POO  """
class PersonajeClan():
    def __init__(self,clan,descripcion):
        self.__nombreClan=clan
        self.__descripcionClan=descripcion
    
    def caracteristicas(self):
        print("El nombre del clan es :",self.__nombreClan," y su descripcion es", self.__descripcionClan)

#----------------------------------------------------------       

#Nomenclatura del punto: Forma para ingresar a cualquier metodo de algun objeto.
class Personaje():
    def __init__(self): #Constructor.
        # Se les debe agregar self para que se puedan identificar como variables de la clase.
        self.__nombrePersonaje="Daniel"
        self.__ataquePersonaje=15 #Encapsulamiento, se realiza con dos rayapiso.
        self.__defensaPersonaje=20 # Solo accesible desde la propia clase, importando o heredando.
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
    def caracteristicas(self):
        print("Estas son las caracteristicas de una personaje")

#----------------------------------------------------------  
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


    def caracteristicas(self):
        super().caracteristicas()  # Se instancia el metodo de la clase Padre, proveniente de su herencia.
        print("El nombre del personaje es :",self.__nombrePersonaje," y su nivel es de ", self.__nivel,"-")
        return " Este es el return"

#----------------------------------------------------------  






miPersonaje= Personaje()
miPersonaje.subirNivel()

print(str(miPersonaje.estadoPersonaje("Esta el estado de mi personaje")))

print("------ Mi Arquero -----------------")
miArquero= PersonajeArquero("Los pikachus"," Es un clan en el que se crian pokemones de tipo pikachu. LOL xd")
print(miArquero.estadoPersonaje("Este es el estado de mi arquero"))

print(miArquero.caracteristicas())


# Principio de sustitucion: Siempre es uno(a), ejemplo: Un arquero siempre es un personaje, un personaje no siempre es un arquerp.

print(isinstance(miArquero,Personaje)) # Devuelve True si el objeto miArquero es de la clase Personaje, lo cual lo es por que su clase hereda de Personaje.


"""------------Despedida ----------------"""
mensajeDespedida=input("Escribe un mensaje de despedida")

