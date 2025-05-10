from statistics import mode, median, mean
import random


#Actividad 1
# Solicitar la edad
edad = int(input("Ingrese tu edad: "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
    
    
#Actividad 2

Nota = int(input("Ingrese la nota del parcial: "))
if Nota >= 6:
    print("Estas aprobado")
else:
    print("Estas desaprobado")
    
#Actividad 3

numero = int(input("Ingrese un numero par: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print('Por favor, ingrese un número par')
    
#Actividad 4

edad = int(input("Ingresa tu edad: "))

if edad < 12:
    print("Es niño")
elif 12 <= edad < 18:
    print("Es Adolescente")
elif 18 <= edad < 30:
    print("Es adulto/a joven")
else:
    print("Es adulto/a")
    
#Actividad 5
contrasena = input("Ingrese una contraseña entre 8 y 14 caracteres: ")

if 8 <= len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, Ingrese una contraseña entre 8 y 14 caracteres")
    
#Actividad 6

numeros_aleatorios = [random.randint(1 , 100) for i in range(50)] 

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)
print("La media de la lista es: ", media, ", la mediana es: ", mediana, " y la moda es: ", moda)

if media > mediana and mediana > moda :
    print("Hay sesgo positivo")
elif media < mediana and mediana < moda :
    print("Hay sesgo negativo")
elif media == mediana and mediana == moda : 
    print("Sin sesgo")
else:
    print('hay error')
    

#Actividad 7
texto = input("Ingrese una frase o palabra: ")

if texto[-1].lower() in "aeiou":
    texto += "!"
print(texto)


#Actividad 8
nombre = input("Ingresa tu nombre: ")
opcion = int(input('Ingresa el numero de la opcion deseada para tu nombre (1. Para mayuscula 2. Para minuscula 3. Para la primer letra en mayuscula): '))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.capitalize())
else:
    print("Opcion no valida")
    
#Actividad 9

intensidad = int(input("Ingrese la magnitud del terremoto: "))

if intensidad < 3 :
    print("Fue muy leve (imperceptible)")
elif 3 <= intensidad < 4:
    print("Leve(Ligeramente perceptible)")
elif 4 <= intensidad < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= intensidad < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= intensidad < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")
    
#Actividad 10

hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").strip().upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))


if hemisferio not in ["N", "S"]:
    print("Hemisferio no válido.")
else:
    fecha = (mes, dia)

    if (fecha >= (12, 21) or fecha <= (3, 20)):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (fecha >= (3, 21) and fecha <= (6, 20)):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (fecha >= (6, 21) and fecha <= (9, 20)):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    elif (fecha >= (9, 21) and fecha <= (12, 20)):
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"

    if hemisferio == "N":
        print(f"Estás en {estacion_norte}.")
    else:
        print(f"Estás en {estacion_sur}.")
