distancia=(int(input("Cual es la distancia del viaje: ")))
precioGasofia=(float(input("Cuál es el precio de la gasolina en este dia: ")))

velocidadConstante=int(100)
consumoporlitro=int(12)

tiempotardado=((distancia/velocidadConstante)*3600)
horas=(int(tiempotardado/3600))
minutos=int((tiempotardado-(horas*3600))/60)

consumogenerado=(distancia/consumoporlitro)
saldogenerado=(consumogenerado*precioGasofia)
saldofinal=("{0:.2f}".format(saldogenerado))

respuesta=("Su viaje durara {} horas, {} minutos y tendra un costo de ${}")

print(respuesta.format(horas,minutos,saldofinal))
