#Actividad 1

for i in range (0 , 101, 1):
    print(i)

#Actividad 2
numero_entero = input("Ingrese un número entero: ")

if numero_entero.startswith('-'):
    numero_entero = numero_entero[1:] 

cantidad_digitos = len(numero_entero)

if numero_entero.isdigit() or (numero_entero.startswith('-') and numero_entero[1:].isdigit()):
    print(f"El número ingresado tiene {cantidad_digitos} dígitos.")
else:
    print("La entrada no es un número entero válido.")   
    
#Actividad 3
try:
    numero1 = int(input("Ingrese el primer valor entero: "))
    numero2 = int(input("Ingrese el segundo valor entero: "))

    suma = 0

    if numero1 < numero2:
        for numero in range(numero1 + 1, numero2):
            suma += numero
        print(f"La suma de los enteros entre {numero1} y {numero2} (excluidos) es: {suma}")
    elif numero2 < numero1:
        for numero in range(numero2 + 1, numero1):
            suma += numero
        print(f"La suma de los enteros entre {numero2} y {numero1} (excluidos) es: {suma}")
    else:
        print("Los valores ingresados son iguales, no hay números entre ellos.")

except ValueError:
    print("Error: Por favor, ingrese números enteros válidos.")
    
    
#Actividad 4
total = 0
print("Ingrese números enteros para sumar. Ingrese 0 para detener.")

while True:
    try:
        entrada = input("Ingrese un número: ")
        numero = int(entrada)

        if numero == 0:
            break 
        else:
            total += numero
            print(f"Total acumulado: {total}")

    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")

print(f"\nTotal final: {total}")

#actividad 5
import random

numero_secreto = random.randint(0, 9)
intentos = 0

print("¡Bienvenido al juego de adivinar el número!")
print("Intenta adivinar un número entero entre 0 y 9.")

while True:
    try:
        intento_str = input("Ingresa tu intento: ")
        intento = int(intento_str)
        intentos += 1

        if intento < numero_secreto:
            print("¡Demasiado bajo! Intenta de nuevo.")
        elif intento > numero_secreto:
            print("¡Demasiado alto! Intenta de nuevo.")
        elif intento == numero_secreto:
            print(f"¡Felicidades! ¡Adivinaste el número {numero_secreto} en {intentos} intentos!")
            break 
        else:
            print("Por favor, ingresa un número entre 0 y 9.")

    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")
    except: 
        print("Ocurrió un error inesperado.")

print("¡Gracias por jugar!")


#Actividad 6
for i in range (100 , 0, -1):
    print(i)
    
#Actividad 7
try:
    limite = int(input("Ingrese un número entero positivo: "))

    if limite < 0:
        print("Por favor, ingrese un número entero positivo.")
    else:
        suma = sum(range(limite + 1))
        print(f"La suma de los números desde 0 hasta {limite} es: {suma}")

except ValueError:
    print("Error: Por favor, ingrese un número entero válido.")
    
    
#Actividad 8
cantidad_numeros = 100

numeros = []
pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Por favor, ingrese {cantidad_numeros} números enteros:")

for i in range(cantidad_numeros):
    while True:
        try:
            entrada = input(f"Ingrese el número {i + 1}: ")
            numero = int(entrada)
            numeros.append(numero)
            break  
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\n--- Resultados ---")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")

#Actividad 9
cantidad_numeros = 100
numeros = []
suma = 0

print(f"Por favor, ingrese {cantidad_numeros} números enteros:")

for i in range(cantidad_numeros):
    while True:
        try:
            numero = int(input(f"Ingrese el número {i + 1}: "))
            numeros.append(numero)
            suma += numero
            break 
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

if cantidad_numeros > 0:
    media = suma / cantidad_numeros
    print(f"\nLa media de los {cantidad_numeros} números ingresados es: {media}")
else:
    print("No se ingresaron números, no se puede calcular la media.")
    
    
#Actividad 10
entrada_str = input("Ingrese un número entero: ")

if entrada_str.startswith('-'):
    signo = '-'
    numero_str = entrada_str[1:]
else:
    signo = ''
    numero_str = entrada_str

numero_invertido_str = signo + numero_str[::-1]

print(f"El número invertido es: {numero_invertido_str}")