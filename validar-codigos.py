claves=[21,31,41,51]
pedirCodigo=int(input("Dime un numero: "))

if pedirCodigo in claves:
	print("codigo no valido")
else:
	print("codigo valido")
	claves.append(pedirCodigo)

print(claves)
