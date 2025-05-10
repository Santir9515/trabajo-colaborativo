def mostrar_resultado(nombre_operacion, resultado, bit_resultado):
    print(f"{nombre_operacion}:")  # Imprime el nombre de la operación como encabezado
    print(f"  Decimal: {resultado}")  # Muestra el resultado en forma decimal (ej. 5)
    print(f"  Binario: {bit_resultado}")  # Muestra el resultado en binario (ej. 0b101)
    print()  # Imprime una línea en blanco para separar visualmente los resultados

# Función principal que contiene la lógica del programa
def main():
    
    print("=== Calculadora de Operaciones Bit a Bit ===")

    try:
        
        # input() devuelve un string, por eso usamos int() para convertirlo a entero
        num1 = int(input("Ingrese el primer número entero: "))

        num2 = int(input("Ingrese el segundo número entero: "))

        resultado_and = num1 & num2
        
        resultado_or = num1 | num2

        resultado_xor = num1 ^ num2

        print("\n--- Resultados ---")

        # Convertimos el resultado a binario con bin() para mostrar cómo se ve en forma binaria

        mostrar_resultado("AND", resultado_and, bin(resultado_and))
        mostrar_resultado("OR", resultado_or, bin(resultado_or))
        mostrar_resultado("XOR", resultado_xor, bin(resultado_xor))

    except ValueError:
        print("Error: Por favor, ingrese solo números enteros.")

if __name__ == "__main__":
    main()