"""#! Impuestos.
    El ciudadano Manuel tiene que pagar impuestos.
    El ciudadano Fayle NO tiene que pagar.
    El ciudadano Lesly tiene que pagar impuestos.
    El ciudadano Mario NO tiene que pagar.
"""
class Persona():
    def __init__(self):
        #? Atributos.
        self.nombre = input("¿Cual es tu nombre?: ")
        self.edad = int(input("¿Cual es tu edad?: "))

    #? Metodos.
    def imprimir(self):
        print(f'Hola {self.nombre} de {self.edad} años de edad.\n')


class Ciudadano(Persona):
    def __init__(self):
        super().__init__()
        self.deposito = float(input("¿Cual es tu deposito?: "))
    
    def imprimir(self):
        print(f'Tu deposito es de: {self.deposito}')

    def impuesto(self):
        if self.deposito > 4000.0:
            print(f'El ciudadano {self.nombre} tiene que pagar impuestos.')
        else:
            print(f'El ciudadano {self.nombre} NO tiene que pagar.')

persona = Ciudadano()
#persona.imprimir()
persona.impuesto()