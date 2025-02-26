from Pokemones.Pokemon import Pokemon
from Pokemones.IFuego import IFuego

# Clase derivada de Pokemon
class Charmander(Pokemon, IFuego):
    def __init__(self, peso, sexo):
        super().__init__("004", "Charmander", peso, sexo, 1, "fuego")

    def atacarPunioFuego(self):
        print(f"Soy {self.nombre} y estoy atacando con Punio de Fuego")

    def atacarAscuas(self):
        print(f"Soy {self.nombre} y estoy atacando con Ascuas")

    def atacarLanzaLlamas(self):
        print(f"Soy {self.nombre} y estoy atacando con Lanza LLamas")