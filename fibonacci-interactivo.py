def fibonacci_iterativo(posicion, debe_imprimir):
    actual = 0
    siguiente = 1
    for x in range(posicion + 1):
        if debe_imprimir:
            print(str(actual) + ",", end="")
        temporal = actual
        actual = siguiente
        siguiente = siguiente + temporal
    return temporal



posicion = 20
# Imprimir sin importar el resultado
print(f"Imprimiendo serie hasta posicion {posicion}")
fibonacci_iterativo(posicion, True)
