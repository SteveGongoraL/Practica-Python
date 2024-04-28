def mayor_edad(edad):
    if edad <18:
        return("Es menor de edad")
    else:
        return("Es mayor de edad")

valor= int(input("Dime tu edad: "))
#print (mayor_edad(valor))
print(f" Con la edad de {valor}, el diagnostico es que: {mayor_edad (valor)}")
