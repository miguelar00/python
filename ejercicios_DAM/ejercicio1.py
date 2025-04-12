def validacion_nombre(nombre):
    if len(nombre) < 6:
         print("El nombre de usuario debe contener al menos 6 caracteres.​")
    elif  len(nombre)> 12:
        print("El nombre de usuario no puede contener más de 12 caracteres")
    elif not nombre.isalnum():
             print("El nombre de usuario puede contener solo letras y números")
    else:
         print("Bienvenido" , nombre)
       
        

user = input("Introduce un nombre : ")

validacion_nombre(user)