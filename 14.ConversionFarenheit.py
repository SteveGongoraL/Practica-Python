gradosFarenheit= float(input("Dime a cuantos grados farenheit estamos: "))
#gradosFarenheit=float(gradosFarenheit)

gradosCelsius= ((gradosFarenheit-32)/1.8000)

salida="{} °F es igual a {} °C"
print(salida.format(gradosFarenheit, gradosCelsius))
