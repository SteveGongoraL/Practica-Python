montoRenta=float(input("Cual es el monto deseado: "))

isrPagar=(montoRenta*0.22)
ivaPagar=(montoRenta*0.16)
totalPagar1=(montoRenta +isrPagar +ivaPagar)
totalPagar2=(montoRenta +ivaPagar)


salida1=("La renta mensual es: ${} \nEl IVA es: ${} \nEl ISR es: ${} \nY el total a pagar es: ${}")
salida2=("La renta mensual es: ${} \nEl IVA es: ${} \nEl ISR es: $0 \nY el total a pagar es: ${}")

if (montoRenta>3000):
    print(salida1.format(montoRenta,ivaPagar,isrPagar,totalPagar1))
else:
    print("Usted no paga ISR ")
    print(salida2.format(montoRenta,ivaPagar,totalPagar2))

