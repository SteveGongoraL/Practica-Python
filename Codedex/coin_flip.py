#Lanzar moneda.

import random

num = random.randint(0,1) #Un numero random del 0 al 1.

if num > 0.5:
    print("Heads")
else:
    print("Tails")