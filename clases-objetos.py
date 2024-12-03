class Bicicleta:
    def __init__(self, color, cambios, rin): # Atributo.
        self.color = color
        self.cambios = cambios
        self.rin = rin
    
    def frenar(self): # Metodos.
        return "La bicicleta esta frenando."
    
    def avanzar(self):
        return "La bicicleta esta en movimiento."
    
    def girar(self):
        return "La bicicleta esta girando."


urbana = Bicicleta("Rojo", 8, 27.5) # Objetos.
hibrida = Bicicleta("Azul", 1, 29)

print(urbana.color)
print(urbana.girar()) # Los metodos tienen que llevar ().
print(hibrida.cambios)



# Ejemplo con animales.
class Animales:
    # Atributos.
    def __init__(self,nombre,edad,peso):
        self.nombre = nombre # Publico.
        self._edad = edad # Protegido, solo es accesible dentro de la clase y subclases.
        self.__peso = peso # Privado, solo se puede acceder dentro de la clase.
    
    # Metodos.
    def caminar(self):
        return "Esta caminando."
    
    def comer(self):
        return "Esta comiendo."
    
    def dormir(self):
        return "Esta dormiendo."

gato = Animales("Manchas",1,4)
perro = Animales("Tony",2,20)
lobo = Animales("Apolo",5,25)

print(gato.nombre)
print(perro.nombre)
print(lobo.caminar())
