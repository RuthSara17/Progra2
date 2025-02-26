from Animales.Animal import Animal

# Clase derivada de Animal
class Caballo(Animal):
    def __init__(self, color, genero, raza, nombre=""):
        super().__init__("caballo", color, genero)
        self.nombre = "S/N" if nombre == "" else nombre
        self.raza = raza

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        super().mostrar_informacion()

    def comer(self):
        print(f"El caballo: '{self.nombre}' de raza {self.raza} esta comiendo")

    def correr(self):
        print(f"El caballo: '{self.nombre}' de raza {self.raza} esta corriendo")