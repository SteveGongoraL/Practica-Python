#Formula cuadratica.

a = int(input("Dime el valor de a: "))
b = int(input("Dime el valor de b: "))
c = int(input("Dime el valor de c: "))


root1= (-b + (b**2 - 4*a*c)**0.5) / (2*a)
root2= (-b - (b**2 - 4*a*c)**0.5) / (2*a)

print(f'El resultado 1 es: {root1}')
print(f'El resultado 2 es: {root2}')