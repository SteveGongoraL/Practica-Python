#lista_original=[2,3,4,5,6,7,8,9]
#lista_doble=[x+x for x in lista_original if x % 2 ==0]
#print(lista_doble)


palabra=input("Dime la palabra que deseas: \n")
for i in range(len(palabra),0,-1): # Inicias, Detienes(no lo incluye), Incremento.
    print (palabra[i-1])


