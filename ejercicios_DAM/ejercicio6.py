def espalindromo(palabra):
    if palabra == palabra[::-1]:
        print("Es palíndromo")
    else:
        print("No es palíndromo")

cadena = input("Introduce una palabra: ")
espalindromo(cadena)
