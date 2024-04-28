import random
CANIDAD_VARIANTES = 4

banco_reactivos_teoricos= {1:"Pregunta uno",2:"Pregunta dos",3:"Pregunta tres",4:"Pregunta cuatro",5:"Pregunta cinco",6:"Pregunta seis",7:"Pregunta siete",8:"Pregunta ocho",9:"Pregunta nueve",10:"Pregunta diez"}
banco_reactivos_practicos={1:"Pregunta uno",2:"Pregunta dos",3:"Pregunta tres",4:"Pregunta cuatro"}

for turno in range(1, CANIDAD_VARIANTES+1):
    sub_lista_teorica= random.sample(list(banco_reactivos_teoricos),8)
    sub_lista_practica= random.sample(list(banco_reactivos_practicos), 2)

    print(f"\n *** Variante {turno} ***")
    print("Parte teorica:")
    for elemento in sub_lista_teorica:
        print(banco_reactivos_teoricos[elemento])

    print("\nParte practica:")
    for elemento in sub_lista_practica:
        print(banco_reactivos_practicos[elemento])
