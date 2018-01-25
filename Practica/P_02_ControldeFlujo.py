
"""Control de flujo 

- No existe el Switch
- Concatenacion de operadores logicos.
"""
#-------- Operador Ternario------
x='@'
validacion=True if x=='@' else False # Esta es la sintaxis de un operador ternario.s variable = objetoVerdero condicionIf condicionElse objetoFalso

print("Validacion de un operador ternario.",validacion)
#----------------------------------

#Sintaxis de un control de flujo, condicional.

numeroFlujo=15

if 0<numeroFlujo<16: 
    print("El numero "+ str(numeroFlujo)+" esta entre los rangos 0 y 16")
    

elif numeroFlujo<=0:
       print("El numero "+ str(numeroFlujo) + " es negativo ")  
else :
    
    print("El numero "+ str(numeroFlujo) + " no esta entre el rango.")


generoPersona="MaScUlino".lower(); # Convierte en minuscula la cadena de texto.

if generoPersona in ("masculino","femenino"): # Es verdaderp si la variable es igual a alguna de las dos opciones.

    print("El genero es correcto")

else:
    print("Genero incorrecto")

edadMascota1=4
nombreMascota=""    

#and,or,not
if 100>edadMascota1>0 and nombreMascota!="": # Se deben cumplir ambas condiciones.
    
    print("Tu mascota llamada "+nombreMascota+" tiene una edad de "+str(edadMascota1))
else:
    print(" Error, la edad o el nombre de la mascota es invalido")

    """------------Despedida ----------------"""
mensajeDespedida=input("Escribe un mensaje de despedida")

