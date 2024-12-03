
#TODO: Clase padre.
class Vehiculo():
    def __init__(self, matricula, modelo, marca, color):
        self.matricula = matricula
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.avanza = False
        self.frena = False
        self.gira = False
    
    def avanzar(self):
        self.avanza = True
    
    def frenar(self):
        self.frena = True
    
    def girar(self):
        self.gira = True
    
    def imprimir(self):
        print(f'Matrciula: {self.matricula} \nModelo: {self.modelo} \nMarca: {self.marca} \nColor: {self.color}'
            f'\nAvanzar: {self.avanza} \nFrenar: {self.frena} \nGirar: {self.gira}')

#TODO: Clase hija.
class Moto(Vehiculo):
    def __init__(self, matricula, modelo, marca, color, cilindraje):
        super().__init__(matricula, modelo, marca, color)
        self.cilindraje = cilindraje

moto1 = Moto("SBGL2000",2008,"Yamaha","Negro",150)
moto1.avanzar()
#TODO: Imprimir.
print(f'Cilindraje: {moto1.cilindraje}')
moto1.imprimir()
