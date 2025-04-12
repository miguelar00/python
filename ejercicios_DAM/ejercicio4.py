def contar_vocal(palabra):
    vocales = ["a","A","e","E","i","I","o","O","u","U"]
    contador = 0
    for i in palabra:
        if i in vocales:
            contador += 1
    print("Tu palabra tiene" , contador , "vocales")
        

user = input("Introduce una palabra: ")

contar_vocal(user)