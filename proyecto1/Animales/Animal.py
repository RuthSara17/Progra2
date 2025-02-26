# Clase base

class Animal:
    def __init__(self, especie, color, genero):
        self.especie = especie;
        self.color = color;
        self.genero = genero;

    def mostrar_informacion(self):
        print(f"Especie: {self.especie}")
        print(f"Genero: {self.genero}")
        print(f"Color: {self.color}")

    def comer(self):
        print(f"El animal de especie: {self.especie}, de color: {self.color}, esta comiendo")
    
    def correr(self):
        print(f"El animal de especie: {self.especie}, de color: {self.color}, esta corriendo")
