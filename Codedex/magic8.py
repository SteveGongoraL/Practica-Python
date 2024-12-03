#Magic 8 ball.

import random

question=input("¿Que deseas saber?: ")
n= random.randint(1,9)

if n==1:
    print("Sí, definitivamente.")
elif n==2:
    print("Es decididamente así.")
elif n==3:
    print("Sin duda alguna.")
elif n==4:
    print("Respuesta confusa, inténtalo de nuevo.")
elif n==5:
    print("Vuelve a preguntar más tarde.")
elif n==6:
    print("Mejor no decírtelo ahora.")
elif n==7:
    print("Mis fuentes dicen que no.")
elif n==8:
    print("Perspectivas no tan buenas.")
else:
    print("Muy dudoso.")

#print('Question:     ' + question)
#print('Magic 8 ball: ' + answer)