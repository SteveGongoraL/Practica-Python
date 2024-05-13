import collections
separador = ("°°°" * 40) + "\n"
# FIFO

# Usando cola con lista
cola_con_lista = list()
for cantidad in range(5):
    cola_con_lista.append(input("Nombre del recien llegado: "))
# Sacar elementos de la lista
print("Procedemos a retirarlos de la cola")
while cola_con_lista:
    # Usando pop(0) saca el primer elemento
    print(f"Quitando el elemento: {cola_con_lista.pop(0)}")
    print(cola_con_lista)
print(separador)


# Usando cola con objeto deque()
cola_con_deque= collections.deque()
for cantidad in range(5):
    cola_con_deque.append(input("Nombre del recien llegado: "))
# Quitando elementos
print("Procedemos a retirarlos de la cola")
while cola_con_deque:
    # Se utiliza popleft() si es un objeto deque
    print(f"Quitando el elemento: {cola_con_deque.popleft()}")
    print(cola_con_deque)
