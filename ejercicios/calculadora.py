print("----------------CALCULADORA DE MIGUEL----------------")

while True:
    print("SUMA")
    print("RESTA")
    print("MULTIPLICACION")
    print("DIVISION")
    print("SALIR")
    
    seleccion = input("Introduzca una opcion del menu: ")
    
    if seleccion == "SUMA":
        n1 = int(input("Introduzca el primer numero : "))
        n2 = int(input("Introduzca el segundo numero : "))
        suma = n1 + n2
        print("EL RESULTADO ES : " , suma)
        
    elif seleccion == "RESTA":
        n1 = int(input("Introduzca el primer numero : "))
        n2 = int(input("Introduzca el segundo numero : "))
        resta = n1 - n2
        print("EL RESULTADO ES : " , resta)
        
        
    elif seleccion == "MULTIPLICACION":
        n1 = int(input("Introduzca el primer numero : "))
        n2 = int(input("Introduzca el segundo numero : "))
        multiplicacion = n1 * n2
        print("EL RESULTADO ES : " , multiplicacion)
        
    elif seleccion == "DIVISION":
        n1 = int(input("Introduzca el primer numero : "))
        n2 = int(input("Introduzca el segundo numero : "))
        
        if n2 == 0:
            print("NO SE PUEDE DIVIR ENTRE 0!")
        else: 
             division = n1 / n2
             print("EL RESULTADO ES : " , division)    
        
    elif seleccion == "SALIR":
        break
    
    else:
        print("OPCION INVALIDA, ESCRIBA UNA OPCION DEL MENU")         