palabra= input(str("Dime la palabra que desees:\n"))
alRevez=(palabra[::-1])

if palabra==alRevez:
    print(f"La palabra {palabra}: es un polindromo")
else:
    print(f"La palabra {palabra}: no es un polindromo")