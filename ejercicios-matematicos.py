import math
separador = ("----" * 40) + "\n"
invalido= ("Escoje un valor valido\n")
i=1

def fib(n):
    a=1
    b=1
    if n==1:
        print("0")
    elif n==2:
        print("0","1")
    else:
        print("0")
        print(a)
        print(b)
        for x in range(n-3):
            total= a+b
            b=a
            a=total
            print(total)

while i==1:
    opcion=int(input("\n¿Que deseas realizar?: \n1)- Ingresar a Calculadora. \n2)- Salir.\n"))
    if opcion==1:
        problema=int(input("\nBuenas, ¿A que problema quiere entrar?: \n1)- Residuo. \n2)- Calcular Areas. \n3)- Raiz y Elevación. \n4)- Serie Fibonacci. \n5)- Calculo de Divisas.\n"))
        if problema==1:
            v1=int(input("Dime el primer numero: "))
            v2=int(input("Dime el segundo numero: "))
            residuo=v1%v2
            print(f"El residuo de {v1} entre {v2} es igual a: {residuo}\n")

        elif problema==2:
            figura=int(input("\n¿De que figura desea conocer el area?: \n1)- Cuadrado. \n2)- Rectangulo. \n3)- Circulo.\n"))
            if figura==1:
                lado=float(input("\n¿Cual es la longitud de uno de sus lados?: "))
                area=lado**2
                print(f"El area de un cuadrado que mide {lado} de lado es igual a: {area}\n")
            elif figura==2:
                base=float(input("¿Canto mide la base del rectangulo?: "))
                altura=float(input("¿Caunto mide la altura del rectangulo?: "))
                area=base*altura
                print(f"El area del rectangulo con una base de {base} y una altura de {altura} es igual a {area}\n")
            elif figura==3:
                r=float(input("¿Cual es el radio del circulo?: "))
                area=(3.14*r)**2
                print(f"El area de un circulo con radio de {r} es igual a {area}\n")
            else:
                print(invalido)

        elif problema==3:
            n1=float(input("¿Me podria proporcionar un numero?: "))
            n2=int(input("¿A que potencia desea elevar la raiz de su numero?: "))
            rz=math.sqrt(n1)
            resultado= rz**n2
            print(f"El resultado de sacar raiz a {n1} y despues elevarlo a la {n2} potencia es: {resultado}\n")

        elif problema==4:
            lim=int(input("¿Cuantos numeros de Fibonacci quiere que se muestren?: "))
            fib(lim)

        elif problema==5:
            divisa=float(input("\n¿Cual es la cantidad que desea convertir?: "))
            divisa2=int(input("\n¿A que valor divisa desea convertirlo?: \n1)- Dolar Canadiense. \n2)- Yen. \n3)- Euro. \n4)- Libra Esterlina.\n"))
            if divisa2==1:
                canadiense=0.062*divisa
                print(f"La divisa en dolares canadienses es: {canadiense}")
            elif divisa2==2:
                yen=5.40*divisa
                print(f"La divisa en yen es: {yen}")
            elif divisa2==3:
                euro=0.042*divisa
                print(f"La divisa en euro es: {euro}")
            elif divisa2==4:
                libra=0.036*divisa
                print(f"La divisa en libra esterlina es: {libra}")
            else:
                print(invalido)

        else:
            print(invalido)
    elif opcion==2:
        print("Gracias =)")
        i=0
    else:
        print(invalido)
