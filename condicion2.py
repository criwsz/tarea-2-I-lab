edad=int(input("Ingrese su edad \n")) 
if edad >=18: #esto es una condicion anindada de varias opciones 
    if edad >=65:
        print("Usted es un adulto mayor")
    else:
        print("Usted es un adulto")
else:
    if edad>3:  
        print("Usted es menor de edad")
    else: 
        print("Es un bebé")