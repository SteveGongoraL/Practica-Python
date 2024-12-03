palabra = input("Dime la palabra que deseas conocer: ")
#palabra_revez= palabra[::-1]

if palabra == palabra[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
