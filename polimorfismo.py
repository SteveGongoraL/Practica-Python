class Gato():
    def sonido(self):
        print("MIAAAAUU")

class Perro():
    def sonido(self):
        print("GUAUF")

class Lobo():
    def sonido(self):
        print("AAAAUUU")

def EscucharSonido(animal):
    animal.sonido()

gato1 = Gato()
perro1 = Perro()
lobo1 = Lobo()

EscucharSonido(lobo1)