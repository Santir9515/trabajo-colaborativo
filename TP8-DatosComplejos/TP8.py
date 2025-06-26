#Actividad 1
precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

#Actividad 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800
print(precios_frutas)

#Actividad 3 
frutas = list(precios_frutas.keys())
print(frutas)

#Actividad 4
agenda = {}

for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el numero de telefono de {nombre}: ")
    agenda[nombre] = numero
    
consulta = input("Ingrese el nombre del contacto a consultar: ")

if consulta in agenda:
    print(f"El numero de {consulta} es: {agenda[consulta]}")
else:
    print(f"No se encontro el contacto con nombre '{consulta}'. ")

#Actividad 5

frase = input("Ingrese una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

conteo_palabras = {}

for palabra in palabras:
    if palabra in conteo_palabras:
        conteo_palabras[palabra] += 1
    else:
        conteo_palabras[palabra] = 1

print("Cantidad de veces que aparece cada palabra:", conteo_palabras)

#Actividad 6
notas_alumnos = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")

    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota {j+1} de {nombre}: "))
        notas.append(nota)

    notas_alumnos[nombre] = tuple(notas)

for alumno, notas in notas_alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {alumno} es: {promedio:.2f}")
    
#Actividad 7
notas_parcial1 = {
    'Ana': 7,
    'Luis': 5,
    'Marta': 8,
    'Jorge': 4,
    'Sofia': 6
}

notas_parcial2 = {
    'Ana': 6,
    'Luis': 7,
    'Marta': 5,
    'Jorge': 8,
    'Sofia': 4
}

aprobados_p1 = {alumno for alumno, nota in notas_parcial1.items() if nota >= 6}
aprobados_p2 = {alumno for alumno, nota in notas_parcial2.items() if nota >= 6}

ambos = aprobados_p1.intersection(aprobados_p2)
print("Alumnos que aprobaron ambos parciales:", ambos)

solo_uno = aprobados_p1.symmetric_difference(aprobados_p2)
print("Alumnos que aprobaron solo uno de los dos parciales:", solo_uno)

al_menos_uno = aprobados_p1.union(aprobados_p2)
print("Alumnos que aprobaron al menos un parcial:", al_menos_uno)

#Actividad 8
stock = {
    'manzana': 10,
    'banana': 5,
    'pera': 8
}

while True:
    print("\nOpciones:")
    print("1. Consultar stock de un producto")
    print("2. Agregar unidades al stock de un producto existente")
    print("3. Agregar un nuevo producto")
    print("4. Salir")

    opcion = input("Elija una opción (1-4): ")

    if opcion == '1':
        producto = input("Ingrese el nombre del producto a consultar: ").lower()
        if producto in stock:
            print(f"Stock de {producto}: {stock[producto]} unidades.")
        else:
            print(f"El producto '{producto}' no existe en el stock.")

    elif opcion == '2':
        producto = input("Ingrese el nombre del producto para agregar unidades: ").lower()
        if producto in stock:
            try:
                unidades = int(input("Ingrese la cantidad de unidades a agregar: "))
                if unidades > 0:
                    stock[producto] += unidades
                    print(f"Nuevo stock de {producto}: {stock[producto]} unidades.")
                else:
                    print("Debe ingresar un número positivo.")
            except ValueError:
                print("Cantidad inválida, debe ser un número entero.")
        else:
            print(f"El producto '{producto}' no existe en el stock.")

    elif opcion == '3':
        producto = input("Ingrese el nombre del nuevo producto: ").lower()
        if producto in stock:
            print("El producto ya existe. Use la opción 2 para agregar unidades.")
        else:
            try:
                unidades = int(input("Ingrese la cantidad inicial de unidades: "))
                if unidades >= 0:
                    stock[producto] = unidades
                    print(f"Producto '{producto}' agregado con {unidades} unidades.")
                else:
                    print("Debe ingresar un número cero o positivo.")
            except ValueError:
                print("Cantidad inválida, debe ser un número entero.")

    elif opcion == '4':
        print("Saliendo del programa.")
        break

    else:
        print("Opción inválida. Por favor ingrese un número entre 1 y 4.")
        
#Actividad 9
agenda = {}

agenda[('Lunes', '10:00')] = "Reunión con equipo"
agenda[('Martes', '15:30')] = "Consulta médica"
agenda[('Miércoles', '09:00')] = "Clase de matemáticas"

for (dia, hora), evento in agenda.items():
    print(f"{dia} a las {hora} -> {evento}")
    
#Actividad 10
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo'
}

capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print(capitales_paises)


