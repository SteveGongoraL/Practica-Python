# Se importa la clase
from inventario import Producto
# libreria para ordenar objetos en funcion a propiedad
from operator import attrgetter
# libreria para manejo de expresiones regulares
import re

# funcion que valida una expresion regular
def RegEx(texto,expresion):
  coincidencia=re.match(expresion,texto)
  return bool(coincidencia)

# Genero una lista de objetos
Productos=[]

# Agrego varios objetos a la lista
Productos.append(Producto("XL12345","Producto de prueba 45",10,500))
Productos.append(Producto("AB27822","Producto de prueba 22",100,4500))
Productos.append(Producto("MI99999","Producto de prueba 99",25,800))

for prod in Productos:
  print("-----------------------------------")
  prod.muestrainfo()

Productos.sort(key=attrgetter("existencia"), reverse=False)

for prod in Productos:
  print("-----------------------------------")
  prod.muestrainfo()

idproductoRegExp="^([A-Z]{2}[0-9]{5})$"
_idproducto=""
while True:
  _idproducto=input("Codigo de producto:")
  if RegEx(_idproducto,idproductoRegExp):
    break
  else:
    print("El dato no cumple. Intenta de nuevo.")

