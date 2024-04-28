# Define las clases del modelo de inventario

# Se utiliza class para la declaracion de clases
class Producto:
  # Cada variable definida en la clase es una propiedad
  idproducto=""
  descproducto=""
  existencia=0
  precio=0
  # Declaro un constructor
  def __init__(self, idproducto, descproducto,existencia,precio):
    self.idproducto=idproducto
    self.descproducto=descproducto
    self.existencia=existencia
    self.precio=precio
  # Mostrado de datos
  def muestrainfo(self):
    print(self.idproducto)
    print(self.descproducto)
    print(self.existencia)
    print(self.precio)
  def reducirexistencia(self, _cant):
    self.existencia=self.existencia-_cant
