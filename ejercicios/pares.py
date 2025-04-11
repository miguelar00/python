N = int(input("INTRODUCE UN NÚMERO POSITIVO: "))

if N < 0:
    print("PROGRAMA FINALIZADO")
else:
    
    pares = [i for i in range(1, N + 1) if i % 2 == 0]
    
    suma_pares = sum(pares)
    
    print("Lista de números pares:", pares)
    print("Suma de los números pares:", suma_pares)
