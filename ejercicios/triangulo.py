# Pedimos al usuario un número entero positivo
N = int(input("INTRODUCE UN NÚMERO: "))

# Variable para ir acumulando la suma total de los números impresos
suma_total = 0

# Bucle externo: controla cuántas filas va a tener el triángulo (de 1 hasta N, inclusive)
for i in range(1, N + 1):
    
    # Bucle interno: imprime los números del 1 hasta el número de la fila actual (i)
    for j in range(1, i + 1):
        print(j, end=' ')       # Imprime j en la misma línea, separado por un espacio
        suma_total += j         # Acumula el número a la suma total

    print()  # Hace un salto de línea después de imprimir una fila completa

# Al finalizar todos los bucles, imprimimos la suma total de todos los números
print("Suma total:", suma_total)

#NO HE CONSEGUIDO HACER ESTE EJERCICIO, ESTA HECHO POR IA