total=int(input("Ingrese el total de la factura \n"))
comision= 0.05
if total >= 10000:
    fact=total*comision
    resultado= fact+total

    print("El total con comision es" ,resultado)
else: 
    print("No se cobrará comisión")