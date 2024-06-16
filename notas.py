n1=int(input("Ingrese nota 1 \n"))
n2=int(input("Ingrese nota 2 \n"))
n3=int(input("Ingrese nota 3 \n"))
n4=int(input("Ingrese nota 4 \n"))

total= n1+n2+n3+n4
resultado= total/4

if resultado <= 10:
    print("Su nota es: F")
else:
    if resultado <= 20:
        print("Su nota es: E")
    else:
        if resultado <= 30:
            print("Su notas es: D")
        else: 
            if resultado <= 40: 
                print("Su nota es: C")
            else: 
                if resultado <= 50 : 
                    print("Su nota es: B")
                else:
                    if resultado <= 100:
                        print("Su nota es: A")
