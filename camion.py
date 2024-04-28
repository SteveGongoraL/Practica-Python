sumatoria_digitos = 0
print ("\n-- Digitos de tu boleto de camion --")

while True:
    digito_boleto = input("Dime un digito de tu boleto: ")
    if digito_boleto == "":
        print(f"Programa terminado. \nLa suma fue de: {sumatoria_digitos}")
        if (digito_boleto == 21):
            print("Te deben un beso" )
        else:
            print("Sigue participando" )
        break
    else:
        sumatoria_digitos += int(digito_boleto)
        print("Para terminar deje el valor vacio.\n")
