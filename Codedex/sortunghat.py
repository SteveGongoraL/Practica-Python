#Juego de Harry Potter.

#Declaracion de variables vacias.
Gryffindor=0
Ravenclaw=0
Hufflepuff=0
Slytherin=0

#Preguntas y asignación de puntos.
q1=int(input("Do you like Dawn or Dusk? \n1) Dawn \n2) Dusk \n"))
if q1==1:
    Gryffindor +=1 #Forma de ir sumandole valores N. 1
    Ravenclaw +=1
elif q1==2:
    Hufflepuff +=1
    Slytherin +=1
else:
    print("Wrong input")

q2=int(input("\nWhen I’m dead, I want people to remember me as: \n1) The Good \n2) The Great \n3) The Wise \n4) The Bold \n"))
if q2==1:
    Hufflepuff = Hufflepuff + 1 #Forma de ir sumandole valores N. 2
elif q2==2:
    Slytherin = Slytherin + 1
elif q2==3:
    Ravenclaw = Ravenclaw + 1
elif q2==4:
    Gryffindor = Gryffindor + 1
else:
    print("Wrong input")

q3=int(input("\nWhich kind of instrument most pleases your ear? \n1) The violin \n2) The trumpet \n3) The piano \n4) The drum \n"))
if q3==1:
    Slytherin +=1
elif q3==2:
    Hufflepuff +=1
elif q3==3:
    Ravenclaw +=1
elif q3==4:
    Gryffindor +=1
else:
    print("Wrong input")

#Validar quien tiene mas puntos.
if Gryffindor >= Slytherin and Gryffindor >= Hufflepuff and Gryffindor >= Ravenclaw:
    print(f'La casa con mas puntos es Gryffindor con: {Gryffindor} puntos.')
elif Slytherin >= Hufflepuff and Slytherin >= Ravenclaw:
    print(f'La casa con mas puntos es Slytherin con: {Slytherin} puntos.')
elif Hufflepuff >= Ravenclaw:
    print(f'La casa con mas puntos es Hufflepuff con: {Hufflepuff} puntos.')
else:
    print(f'La casa con mas puntos es Ravenclaw con: {Ravenclaw} puntos.')


""" print(f'Gryffindor: {Gryffindor}')
print(f'Slytherin: {Slytherin}')
print(f'Hufflepuff: {Hufflepuff}')
print(f'Ravenclaw: {Ravenclaw}')
"""