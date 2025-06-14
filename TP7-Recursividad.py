#Ejercicio 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

limite = int(input("Ingrese un número para mostrar los factoriales desde 1 hasta ese número: "))

print("Factoriales:")
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")

#Ejercicio 2
def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos - 1) + fibonacci(pos - 2)

n = int(input("Ingrese la cantidad de términos de la serie Fibonacci: "))

print("Serie de Fibonacci:")
for i in range(n):
    print(f"F({i}) = {fibonacci(i)}")

#Ejercicio 3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")

#Ejercicio 4
def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un número decimal positivo: "))

binario = decimal_a_binario(numero)
print(f"El número {numero} en binario es: {binario}")
