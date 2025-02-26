from Pokemones.Pokemon import Pokemon
from Pokemones.IPlanta import IPlanta

# Clase derivada de Pokemon
class Bulbasaur(Pokemon, IPlanta):
    def __init__(self, peso, sexo):
        super().__init__("001", "Bulbasaur", peso, sexo, 1, "Planta")

    def atacarParalizar(self):
        print(f"Soy {self.nombre} y estoy atacando con Paralizar")

    def atacarDrenaje(self):
        print(f"Soy {self.nombre} y estoy atacando con Drenaje")

    def atacarHojaAfilada(self):
        print(f"Soy {self.nombre} y estoy atacando con Hoja afilada")

    def atacarLatigoCepa(self):
        print(f"Soy {self.nombre} y estoy atacando con Latigo cepa")