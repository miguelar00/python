def mayordetres(n1 ,n2, n3):
    numeros = [n1,n2,n3]
    mayor = max(numeros)
    return(mayor)
        
n1 = int(input("INTRODUCE EL PRIMER NUMERO: "))
n2 = int(input("INTRODUCE EL SEGUNDO NUMERO: "))
n3 = int(input("INTRODUCE EL TERCER NUMERO: "))

resultado =  mayordetres(n1,n2,n3) 
print(resultado)