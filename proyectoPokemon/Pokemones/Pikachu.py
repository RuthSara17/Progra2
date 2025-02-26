from Pokemones.Pokemon import Pokemon
from Pokemones.IElectrico import IElectrico

# Clase derivada de Pokemon
class Pikachu(Pokemon, IElectrico):
    def __init__(self, peso, sexo):
        super().__init__("001", "Bulbasaur", peso, sexo, 1, "Planta")

    def atacarImpactrueno(self):
        print(f"Soy {self.nombre} y estoy atacando con Impactrueno")

    def atacarPunioTrueno(self):
        print(f"Soy {self.nombre} y estoy atacando con Punio trueno")

    def atacarRayo(self):
        print(f"Soy {self.nombre} y estoy atacando con Rayo")

    def atacarRayoCarga(self):
        print(f"Soy {self.nombre} y estoy atacando con RayoCarga")