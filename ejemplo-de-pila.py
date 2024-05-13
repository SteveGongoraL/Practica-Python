import collections
separador = ("°°°" * 40) + "\n"
# LIFO

# Usando pila con lista
pila_con_lista = list()
for i in range(5):
    pila_con_lista.append(input("Dime el nombre a agregar: "))
# Sacar elemento de la lista
while pila_con_lista:
    # Usando pop() saca el ultimo elemento
    print(f"Quitando el elemento: {pila_con_lista.pop()}")
    print(pila_con_lista)
print(separador)


# Usando pila con objeto deque()
# Siempre es mejor usar un objeto deque
pila_con_deque = collections.deque()
for i in range(5):
    pila_con_deque.append(input("Dime el numero a agregar: "))
# Sacar elemento de la pila
while pila_con_deque:
    print(f"Quitando el elemento: {pila_con_deque.pop()}")
    print(pila_con_deque)
