import random
separador = ("°°°" * 40) + "\n"

# Creando una lista con valores aleatorios
lista_valores_random = [random.randrange(1,101) for valor in range(25)]
print(type(lista_valores_random))
print(f"La lista es:\n {lista_valores_random}")
print(f"El primer elemento es: {lista_valores_random[0]}, el ultimo es: {lista_valores_random[24]} & el valor de enmedio es: {lista_valores_random[13]}")
print(separador)

# Una lista que tiene 4 listas dentro
lista_de_listas= [[random.randrange(1,101) for valor in range (10)] for valor in range(5)]
print(f"La lista es:\n {lista_de_listas}")
print(type(lista_de_listas))
print(f"El primer elemento de la primer sub-lista es:\n {lista_de_listas[0][0]} \nEl ultimo elemento de la ultima sub-lista es:\n {lista_de_listas[4][9]}")
print(separador)

# Imprimiendo el primer elemento de cada sub-lista
print(f"La primera sub-lista es:\n {lista_de_listas[0]}")
print("El primer valor de cada sub-lista es: ")
for listaInterna in lista_de_listas:
    print(listaInterna[0])
print(separador)

# Imprimiendo el ultimo elemento de cada sub-lista
print("El ultimo valor de cada sub-lista es: ")
for listaInterna in lista_de_listas:
    print(listaInterna[-1]) # Si no sabes cuantas columnas pones '-1'
print(separador)
