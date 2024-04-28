import datetime

def IngresaOpcion():
    correcto=False
    num=0

    while(not correcto):
        try:
            num = int(input("Introduce un numero: "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
    return num

#FECHA, FACTURA, ENTRADA, SALIDA, EXISTENCIA, SALDO_ENTRADA, UNITARIO, DEBE, HABER, SALDO
almacen = []

def NuevaEntrada(factura, entrada, precio):
    fecha = datetime.datetime.now()
    fecha = str(fecha.day) + '/' + str(fecha.month) + '/' + str(fecha.year)

    total = entrada * precio

    existencia = entrada
    saldo = total

    if (len(almacen) != 0):
        ultimo = almacen[-1]
        existencia = ultimo[4] + entrada
        saldo = ultimo[9] + total

    nuevo = [fecha, factura, entrada, 0, existencia, entrada, precio, total, 0, saldo]
    almacen.append(nuevo)
    return 'Entrada guardada correctamente'

def SalidaNueva(factura, salida):
    fecha = datetime.datetime.now()
    fecha = str(fecha.day) + '/' + str(fecha.month) + '/' + str(fecha.year)
    pendiente = salida
    cnt = 0

    ultimo = almacen[-1]
    existencia = ultimo[4]
    saldo = ultimo[9]

    saldoAlmacen = 0
    for movimiento in almacen:
        saldoAlmacen = saldoAlmacen + movimiento[5]
    
    if saldoAlmacen < salida:  #no hay saldo en almacen
        return 'Sin unidades suficientes en almacen. Unidades: ' + str(saldoAlmacen)  

    mensaje = ''
    PrecioTotal = 0.0

    for movimiento in almacen:
        saldo_entrada = movimiento[5]
        precio_unitario = movimiento[6]
        if (saldo_entrada != 0):  #ENTRADA TIENE SALDO
            if pendiente > saldo_entrada:
                pendiente = salida - saldo_entrada
                salida_actual = saldo_entrada
                existencia = existencia - salida_actual
                total = precio_unitario * salida_actual
                saldo = saldo - total
                almacen[cnt][5] = 0

                mensaje = mensaje + '\nUnidades: ' + str(salida_actual) + '. Precio Unitario: ' + str(precio_unitario) + '. Precio: ' + str(total)
                PrecioTotal = PrecioTotal + total

                #FECHA, FACTURA, ENTRADA, SALIDA, EXISTENCIA, SALDO_ENTRADA, UNITARIO, DEBE, HABER, SALDO
                nuevo = [fecha, factura, 0, salida_actual, existencia, 0, precio_unitario, 0, total, saldo]
                almacen.append(nuevo)
            else:
                saldo_entrada = saldo_entrada - pendiente
                existencia = existencia - pendiente
                total = precio_unitario * pendiente
                saldo = saldo - total
                almacen[cnt][5] = saldo_entrada

                mensaje = mensaje + '\nUnidades: ' + str(pendiente) + '. Precio Unitario: ' + str(precio_unitario) + '. Precio: ' + str(total)
                PrecioTotal = PrecioTotal + total

                #FECHA, FACTURA, ENTRADA, SALIDA, EXISTENCIA, SALDO_ENTRADA, UNITARIO, DEBE, HABER, SALDO
                nuevo = [fecha, factura, 0, pendiente, existencia, 0, precio_unitario, 0, total, saldo]
                almacen.append(nuevo)

                pendiente = 0
        if (pendiente == 0):
            break
        cnt += 1
    mensaje = mensaje + '\nPrecio total: ' + str(PrecioTotal)
    return mensaje

while True: #not salir:

    print("Buenos Dias,Bienvenido a el sistema de inventario")
    print("1. Entrada de mercancia")
    print("2. Salida de mercancia")
    print("3. Ver tarjeta de almacen")
    print("4. Salir \n")
    
    opcion = IngresaOpcion()

    if (opcion == 1):
        #CODIGO PARA INGRESAR ENTRADA DE MERCANCIA
        factura = input("Factura: ")
        entrada = int(input("Unidades por entrar: "))
        precio_unitario = float(input("Precio unitario: "))

        retorno = NuevaEntrada(factura, entrada, precio_unitario)
        print(retorno)

    if (opcion == 2):
        #CODIGO PARA INGRESAR SALIDA DE MERCANCIA
        if (len(almacen) == 0):
            print('Almacen vacio.')
        else:
            factura = input("Factura: ")
            salida = int(input("Unidades por salir: "))

            retorno = SalidaNueva(factura, salida)
            print(retorno)

    if (opcion == 3):
        #CODIGO PARA VER ALMACEN
        teams_list = ['FECHA', 'FACTURA', 'ENTRADA', 'SALIDA', 'EXISTENCIA', 'SALDO ENTRADA', 'UNITARIO', 'DEBE', 'HABER', 'SALDO']
        data = almacen
        #row_format ="{:>10}" * (len(teams_list) + 1)
        row_format = '{:>10}{:>10}{:>10}{:>10}{:>10}{:>15}{:>15}{:>10}{:>10}{:>10}{:>10}'
        print('   ' + (row_format.format("", *teams_list)).strip())
        for team, row in zip(teams_list, data):
            test = row_format.format(team, *row)
            print((row_format.format('', *row)).strip())

    if (opcion == 4):
        break