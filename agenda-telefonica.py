agenda_telefonica = {"Jose":302944,"Mario":829455,"Angel":829405,"Luis":930594}
menu = 0
print("¡¡AGENDA TELEFONICA 2023!!")

while menu != 5:
    menu=int(input("\n¿Cual opcion deseas realizar?: \n1) Consultar. \n2) Añadir. \n3) Modificar. \n4) Borrar. \n5) Salir.\n"))

    if menu == 1:
        print("\n--Consultar Usuario--")
        nombre = input("¿Cual es el nombre que desea buscar?:\n")
        if nombre in agenda_telefonica:
            print(f'\nEl numero de {nombre} es: {agenda_telefonica[nombre]}.')
        else:
            print("Ese usuario no existe.")
    elif menu == 2:
        print("\n--Añadir--")
        nombre = input("¿Cual es el nombre?:\n")
        if nombre in agenda_telefonica:
            print("\nEl usuario ya se encuentra agregado.")
        else:
            telefono=int(input("¿Cual es el numero de telefono?:\n"))
            agenda_telefonica[nombre] = telefono
            print("Usuario registrado.")
    elif menu == 3:
        print("\n--Modificar--")
        nombre = input("¿Cual es el nombre?:\n")
        if nombre not in agenda_telefonica:
            print("\nEl usuario que esta buscando no existe.")
        else:
            telefono=int(input("¿Cual sera su nuevo numero de telefono?:\n"))
            agenda_telefonica[nombre] = telefono
            print("Usuario actualizado.")
    elif menu == 4:
        print("\n--Borrar--")
        nombre = input("¿Cual es el nombre?:\n")
        if nombre not in agenda_telefonica:
            print("\nEl usuario que esta buscando no existe.")
        else:
            del agenda_telefonica[nombre]
            print("Usuario eliminado.")
    elif menu ==5:
        print("GOOD NIGHT AND GOOD BYE! BANG")
    else:
        print("Escribr una opcion valida.")
