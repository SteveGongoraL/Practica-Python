import sys
separador = ("°°°" * 40) + "\n"

# Utilizando TRY
listaValores = ['x', 0, 4]
print(separador)

for valor in listaValores:
    try:
        print(f"El valor en turno es: {valor}")
        reciproco = 1 / int(valor)
        print(f"El reciproco es {reciproco}")
    # Lo que pasa si se encuentra una excepción
    except ValueError:
        print(f"El valor {valor} no puede ser dividido porque no es un numero.")
    except ZeroDivisionError:
        print(f"La division entre cero no esta permitida.")
    except:
        print(f"Ocurrió un problema {sys.exc_info()[0]}")
        Exception=sys.exc_info()
        for elemento in Exception:
            print(elemento)
    # Lo que se imprimira cuando funcione
    else:
        print("Ahora si funciono bien!! ;) ")
    # Se ejecute siempre
    finally:
        print("°°°°°° Esta linea siempre se ejecutara °°°°°° \n")
