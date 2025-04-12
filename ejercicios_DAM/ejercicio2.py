def validacion_contrasenia(contrasenia):
    if len(contrasenia) < 8:
        print("La contraseña debe tener un minimo de 8 caracteres")
    elif  contrasenia.isupper():
        print("Introduce al menos un caracter en mayuscula")
    elif  contrasenia.islower():
        print("Introduce al menos un caracter en minuscula")
    elif contrasenia.isdigit():
        print("Introduce al menos un caracter numerico")
    elif  contrasenia.isalnum():
        print("Introduce al menos un caracter no alfanumerico")
    elif  contrasenia.isspace():
        print("La contraseña no puede contener espacios en blanco")
    else:
        print("Contraseña creada correctamente")
        
        
user = input("Introduce una contraseña : ")        

validacion_contrasenia(user)        