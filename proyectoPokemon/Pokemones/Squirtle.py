from Pokemones.Pokemon import Pokemon
from Pokemones.IAgua import IAgua

# Clase derivada de Pokemon
class Squirtle(Pokemon, IAgua):
    def __init__(self, peso, sexo):
        super().__init__("001", "Bulbasaur", peso, sexo, 1, "Planta")

    def atacarHidrobomba(self):
        print(f"Soy {self.nombre} y estoy atacando con Hidrobomba")

    def atacarPistolaAgua(self):
        print(f"Soy {self.nombre} y estoy atacando con Pistola de Agua")

    def atacarBurbuja(self):
        print(f"Soy {self.nombre} y estoy atacando con Burbuja")

    def atacarHidropulso(self):
        print(f"Soy {self.nombre} y estoy atacando con Hidropulso")