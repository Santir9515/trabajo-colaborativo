#Actividad 1
multiplos_de_cuatro = list(range(4, 101, 4))
print(multiplos_de_cuatro)

#Actividad 2
lista_inventada = [2,3,8,15,25]
print(lista_inventada[4])

#Actividad 3
lista_principal = []
lista_principal.append(5)
print(lista_principal)
lista_principal.append(15)
print(lista_principal)
lista_principal.append(23)
print(lista_principal)

#Actividad 4
animales = ["perro", "gato", "conejo", "pez"]
print(animales)
animales[1] = "loro"
animales[3] = "oso"
print(animales)

#Actividad 5
#Se crea una lista llamada numeros que contiene los números enteros 8, 15, 3, 22 y 7 en ese orden.
#numeros.remove(max(numeros)): Esta línea realiza dos acciones en una:
#max(numeros): Primero, se utiliza la función max() para encontrar el valor más grande dentro de la lista numeros. En este caso, el valor máximo es 22.
#numeros.remove(...): Luego, se llama al método remove() sobre la lista numeros. El método remove() busca la primera ocurrencia del valor que se le pasa como argumento (que en este caso es el resultado de max(numeros), es decir, 22) y lo elimina de la lista.
#Finalmente, se imprime en la pantalla el contenido actual de la lista numeros después de que el elemento más grande ha sido removido.

#Actividad 6
lista_saltos = list(range(10, 31, 5))
print(lista_saltos[:2])

#Actividad 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "chevrolet"
autos[2] = "fiat"
print(autos)

#actividad 8
dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)

#Actividad 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente (índice 2)
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente (índice 1)
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente (índice 0)
compras[0].remove("pan")

# d) Imprimir la lista resultante por pantalla
print(compras)

#Actividad 10
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)

