
#! Actividad de conversion de moneda con subfunciones funciones.

def conversor(moneda_actual, valor, moneda_a_convertir):
    if moneda_actual == 1:
        def dolarTo():
            if moneda_a_convertir == 1:
                print(f'{valor} dolares equivalen a {valor * 3750} pesos colombianos.')
            elif moneda_a_convertir == 2:
                print(f'{valor} dolares equivalen a {valor * 6.37} yuanes.')
            elif moneda_a_convertir == 3:
                print(f'{valor} dolares equivalen a {valor * 0.76} libras esterlinas.')
            else:
                print("Escoje una moneda valida.")
        dolarTo()
    elif moneda_actual == 2:
        def euroTo():
            if moneda_a_convertir == 1:
                print(f'{valor} euros equivalen a {valor * 4000} pesos colombianos.')
            elif moneda_a_convertir == 2:
                print(f'{valor} euros equivalen a {valor * 6.93} yuanes.')
            elif moneda_a_convertir == 3:
                print(f'{valor} euros equivalen a {valor * 0.83} libras esterlinas.')
            else:
                print("Escoje una moneda valida.")
        euroTo()
    else:
        print("Porfavor escoja una moneda valida.")

print("Bienvenidos al conversor de monedas.")

a_moneda = int(input("\n¿Cual es la moneda que tienes?: \n1) Dolar. \n2) Euro.\n"))
v_moneda = float(input("\n¿Cual es la cantidad que tienes?:\n"))
c_moneda = int(input("\n¿A que moneda deseas convertirlo?: \n1) Pesos Colombianos. \n2) Yuanes. \n3) Libras Esterlinas.\n"))

conversor(a_moneda,v_moneda,c_moneda)