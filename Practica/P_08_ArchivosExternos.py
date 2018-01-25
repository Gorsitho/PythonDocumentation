import io # Biblioteca necesaria para trabajar con archivos externos (Stream)

import pickle # Biblioteca para trabajar serializacion.

""" Archivos externos

- Los archivos externos cumplen como objetivo la persistencias de datos.
 La informacion se mantiene aunque este se cierre.

Pasos para guardar archivos externos:
1.Creacion.
2.Apertura.
3.Manipulacion.
4.Cierre.


"""
archivo_texto=open("archivo.txt","w") #(NombreArchivo.extension, Writting).De esta manera se crea el archivo con la extension dada.

frase=" Una buena noche para escribir un texto."

archivo_texto.write(frase) #Escribe en el archivo.

archivo_texto.close() # Cierra el objeto en memoria.



archivo_texto=open("archivo.txt","r") #(NombreArchivo.extension, reading).De esta manera se lee el archivo con la extension dada.

archivo_texto.seek(5) # Ubicacion del puntero, desde donde empieza a leer.

texto=archivo_texto.read(20) # Se captura archivo abierto y se le asigna a la variable texto. El argumento indica hasta donde leera.

print(texto) 

archivo_texto.close() # Cierra el objeto en memoria.



archivo_texto=open("archivo.txt","r") 

lineaTexto=archivo_texto.readlines() # Se guarda linea a linea en un objeto lista. Sienda cada indice una linea.

print(lineaTexto) 

archivo_texto.close() 



archivo_texto=open("archivo.txt","a") #(NombreArchivo.extension, append).De esta manera se adjunta algo nuevo al archivo.

archivo_texto.write("\n Esta es la linea agregada con el argunmento append") # Se adjunta una nueva linea.

archivo_texto.close() 


archivo_texto=open("archivo.txt","r+") #(NombreArchivo.extension, reading+writting).De esta manera se lee y se escribe el archivo con la extension dada.

listaTexto= archivo_texto.readlines()

listaTexto[1] ="Esta linea de texto ha sido incluido mediante el writelines"

archivo_texto.seek(0)

archivo_texto.writelines(listaTexto)   

archivo_texto.close()



""" Serializacion 

- Guarda en un fichero externo, algun objeto codificado en codigo binario.

"""

# ------------- Serializacion de una coleccion. ---------------

listaMascotas = ["Pelusa","Dorothy","Pepe"] # Lista

ficheroBinario = open("listaMascotas","wb") #(Objeto,Writting binary) 

pickle.dump(listaMascotas ,ficheroBinario) #(ObjetoVolcar, ficheroaDondeVolcar ) Informacion que se quiere volcar, fichero a donde se queire volcar.

ficheroBinario.close()  


ficheroLectura = open("listaMascotas","rb") #(Objeto,Reading binary) 

lista=pickle.load(ficheroLectura) #Carga el archivo que se quiere leer.

print(lista)

ficheroBinario.close()


# ------------- Serializacion de objetos. ---------------


class Mascotas():

    def __init__(self,nombreMascota,edadMascota):
        self.nombreMascota=nombreMascota
        self.edadMascota=edadMascota

    def informacionMascota(self):
        print("* Nombre de la mascota es : ",self.nombreMascota,"\n* Edad : ",self.edadMascota)
       


gatoDaniel= Mascotas("Pelusa",2)

perroJavier= Mascotas("Lulu",7)

listadodeMascotas=[gatoDaniel,perroJavier]

ficheroMascota = open("listadodeMascotas","wb") #(Objeto,Writting binary) 

pickle.dump(listadodeMascotas ,ficheroMascota) #(ObjetoVolcar, ficheroaDondeVolcar ) Informacion que se quiere volcar, fichero a donde se queire volcar.

ficheroMascota.close()  


LecturaFicheroM = open("listadodeMascotas","rb") #(Objeto,Reading binary) 

LecturaMascota=pickle.load(LecturaFicheroM) #Carga el archivo que se quiere leer.
LecturaFicheroM.close()
del(LecturaFicheroM) # Elimina el objeto totalmente.Opcional.

for m in LecturaMascota:
    print(m.informacionMascota()) # Imprime la informacion de cada objeto usando su metodo.






"""------------Despedida ----------------"""
mensajeDespedida=input("Escribe un mensaje de despedida")