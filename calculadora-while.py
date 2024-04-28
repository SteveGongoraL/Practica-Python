separador = ("----" * 40) + "\n"
invalido=print("Debes escojer un valor valido\n")
i=1

while i==1:
    opcion= int(input("¿Que deseas realizar?: \n1)- Ingresar a Calculadora. \n2)- Salir.\n"))

    if opcion==1:
        operacion=int(input("¿Que operacion desea realizar?: \n1)- Suma. \n2)- Resta. \n3)- Multiplicacion. \n4)- Division. \n5)- Residuo.\n"))

        v1=float(input("Dime el primer numero: "))
        v2=float(input("Dime el segundo numero: "))
        if operacion==1:
            suma= v1 + v2
            print(f"El resultado de sumr {v1} + {v2} es igual a: {suma}\n")
        elif operacion==2:
            resta= v1-v2
            print(f"El resulatdo de restar {v1} - {v2} es igual a: {resta}\n")
        elif operacion==3:
            multiplicacion=v1*v2
            print(f"El resulatdo de multiplicar {v1} * {v2} es igual a: {multiplicacion}\n")
        elif operacion==4:
            division=v1/v2
            print(f"El resultado de dividir {v1} entre {v2} es igual a: {division}\n")
        elif operacion==5:
            residuo=v1%v2
            print(f"El residuo resultante entre {v1} y {v2} es igual a: {residuo}\n")
        else:
            print(invalido)

    elif opcion==2:
        print("Gracias =)")
        i=0

    else:
        print(invalido)