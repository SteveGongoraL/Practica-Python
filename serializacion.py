from typing import List
import json

class Persona:
    nombre=""
    apellidos=""
    def __init__(self, nombre, apellidos):
        self.nombre=nombre
        self.apellidos=apellidos
    def muestraInfo(self):
        print("Clase Progra")
        print(self.nombre)
        print(self.apellidos)

class Estudiante(Persona):
    graduacion=0
    def __init__(self, nombre, apellidos, graduacion=2015):
        super().__init__(nombre, apellidos)
        self.graduacion=graduacion
    def muestraInfo(self):
        print("Clase Matematicas")
        print(self.nombre)
        print(self.apellidos)
        print(self.graduacion)
    def derivadoInfo(self):
        print(self.graduacion)

print("----------------------------------------------")
unaPersona=Persona("Miguel","Guerrero")
unaPersona.muestraInfo()
print("----------------------------------------------")
unEstudiante=Estudiante("Melanie","Hernandez")
unEstudiante.graduacion=2019
unEstudiante.muestraInfo()
print("----------------------------------------------")
unEstudiante.derivadoInfo()

Estudiantes=[]
Estudiantes.append(Estudiante("Pablo", "Gongora",2021))
Estudiantes.append(Estudiante("Jose", "Cavazo",2022))
Estudiantes.append(Estudiante("Marcos", "Fernandez",2020))

print(Estudiantes)
json_data = json.dumps(Estudiantes, default=lambda o: o.__dict__, indent=4)
print(json_data)
