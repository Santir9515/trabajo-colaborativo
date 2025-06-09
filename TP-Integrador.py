def cargar_texto(ruta_archivo):
    #Lee el archivo y devuelve una lista de palabras en minúsculas, sin signos de puntuación
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        texto = archivo.read().lower()
    
    palabras = texto.split()
    #Aca limpiamos los signos de puntuacion para evitar errores
    palabras_limpias = [palabra.strip(".,:;()¿?!¡\"'") for palabra in palabras]
    return palabras_limpias

#Vamos a contar la frecuencia de cada palabra usando un diccionario
def contar_frecuencias(lista_palabras):
    frecuencias = {}
    for palabra in lista_palabras:
        #evita palabras vacias
        if palabra:
            if palabra in frecuencias:
                frecuencias[palabra] += 1
            else:
                frecuencias[palabra] = 1
    return frecuencias

#La siguiente función devuelve la frecuencia de una palabra, Si no existe, retorna 0.
def buscar_palabra(frecuencias, palabra):
    return frecuencias.get(palabra.lower(), 0)

#Esta funcion va a devolver una lista de tuplas (palabra, frecuencia) ordenadas de mayor a menor
def ordenar_por_frecuencia(frecuencias): 
    #Esto ayuda a ordenar de mayor a menor la frecuencia de las palabras y ademas si hay empate las ordena alfabeticamente
    return sorted(frecuencias.items(), key=lambda x: (-x[1], x[0])) 

#Esta funcion nos va a ordenar las tuplas alfabeticamente por palabra
def ordenar_alfabeticamente(frecuencias):
    return sorted(frecuencias.items(), key=lambda x: x[0])

if __name__ == "__main__":
    archivo = input("Ruta del archivo de texto (.txt): ")
    palabras = cargar_texto(archivo)
    print(f"\nSe procesaron {len(palabras)} palabras.\n")
    
    frecuencias = contar_frecuencias(palabras)
    
    palabra_buscada = input("Que palabra querés buscar?: ")
    resultado = buscar_palabra(frecuencias, palabra_buscada)
    print(f"La palabra '{palabra_buscada}' aparece {resultado} veces. \n")
    
    print("Top 10 palabras mas frecuentes:")
    top10 = ordenar_por_frecuencia(frecuencias)[:10]
    for palabra, cantidad in top10:
        print(f"{palabra}: {cantidad}")
        
    print("\nPrimeras 10 palabras ordenadas alfabeticamente:")
    orden_alfabetico = ordenar_alfabeticamente(frecuencias)[:10]
    for palabra, cantidad in orden_alfabetico:
        print(f"{palabra}: {cantidad}")