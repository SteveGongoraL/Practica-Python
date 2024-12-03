# Calcular el total en USD.

yuan = float(input('What do you have left in yuan? '))
yen = float(input('What do you have left in yen? '))
won = float(input('What do you have left in won? '))

c1 = yuan*0.14
c2 = yen*0.0076
c3 = won*0.00079

d= c1+c2+c3

print(f'El total en dolares es: ${d}')