# Se almacena un numero y se almacena una vez que es convertido a int.
# int = variable entera como '3'
numero=int(input("Dame un numero entero: "))

# Se almacena en valores booleanos la evaluacion. Si el residual es cero, quiere decir que el numero es multiplo.
esMultiplo3=((numero%3)==0)
esMultiplo5=((numero%5)==0)
esMultiplo7=((numero%7)==0)

# Los parentesis indican que las primeras condiciones son juntas, y que la tercera es independiente.
if ((esMultiplo3 and esMultiplo5) or esMultiplo7):
    print("Correcto. ")
else:
    print("Incorrecto. ")
