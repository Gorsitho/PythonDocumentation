
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

    """------------Despedida ----------------"""
mensajeDespedida=input("Escribe un mensaje de despedida")

