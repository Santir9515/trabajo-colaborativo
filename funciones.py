import math

#Ejercicio 1
def imprimir_hola():
    print("Hola mundo")
    
imprimir_hola()

#Ejercicio 2
def saludar_usuario(nombre):
    print(f"Hola {nombre}")
    
saludar_usuario(input("Ingresa tu nombre: "))    

#Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

informacion_personal(
    input("Ingresa tu nombre: "),
    input("Ingresa tu apellido: "),
    int(input("Ingresa tu edad: ")),
    input("Ingresa tu lugar de residencia: ")
)

#Ejercicio 4
def calcular_area_circulo(radio):
    return math.pi * radio **2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingresa el radio del circulo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El area del circulo es: {area:.2f}")
print(f"El perimetro del circulo es: {perimetro:.2f}")

#Ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 3600

segundos_ingresados = float(input("Ingrese la cantidad de segundos"))

horas = segundos_a_horas(segundos_ingresados)
print(f"{segundos_ingresados} segundos equivalen a {horas:.2f} horas")

#Ejercicio 6
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}: ")
    for i in range (1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
        
numero_ingresado = int(input("Ingrese un numero para ver si tabla de multiplicar"))

tabla_multiplicar(numero_ingresado)

#Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    # Validacion para que b no sea cero para evitar división por cero
    division = a / b if b != 0 else "Indefinido (división por cero)"
    return (suma, resta, multiplicacion, division)

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(a, b)

print("\nResultados de las operaciones básicas:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

#Ejercicio 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)

print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese la temperatura en grados Celsius: "))

fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

#Ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(a, b, c)

print(f"El promedio de los tres números es: {promedio:.2f}")



