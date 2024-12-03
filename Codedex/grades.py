#Verificar calificación.

grade= float(input("Dime cual es la calificación del alumno: "))

if grade >100:
    print("Escribe una calificación valdia")
else:
    if grade >=70:
        print("You passed.")
    else:
        print("You failed.")