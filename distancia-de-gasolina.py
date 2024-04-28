print("\n-- Simulador de costo de gasolina por viaje --")

distancia = (int(input("¿Cual es la distancia del viaje?: ")))
precio_gasolina = (float(input("¿Cuál es el precio de la gasolina en este dia?: ")))

velocidad_constante = 100
consumo_por_litro = 12

tiempo_tardado = ((distancia / velocidad_constante) * 3600)
horas_viaje = (int(tiempo_tardado / 3600))
minutos_viaje = int((tiempo_tardado - (horas_viaje * 3600)) / 60)

consumo_generado = (distancia / consumo_por_litro)
saldo_generado = (consumo_generado * precio_gasolina)

print(f"Su viaje durara {horas_viaje} horas, {minutos_viaje} minutos y tendra un costo de ${saldo_generado}")
