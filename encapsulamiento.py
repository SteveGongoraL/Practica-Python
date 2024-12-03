class Persona:
    def __init__(self, identificacion, nombre, edad): #? Atributos.
        self.__identificacion = identificacion
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self): #? Metodos.
        return "Hola " + self.nombre

    def getIdentificacion(self):
        return self.__identificacion

    def setIdentificacion(self, valor):
        self.__identificacion = valor


persona1 = Persona(12345,"Steve",22) #? Imprimiendo un Objeto.
persona1.setIdentificacion(99999) #? Imprimiendo un metodo SET.



#TODO: Formas de imprimir un atributo privado.
#print(persona1.identificacion) #? Si es publica si funciona.
#print(persona1._Persona__identificacion) #? Si es privada asi puede funcionar.
print(persona1.getIdentificacion()) #? Utilizando GET.

print(persona1.nombre)
print(persona1.edad)
print(persona1.saludar()) #? Imprimiendo un metodo.