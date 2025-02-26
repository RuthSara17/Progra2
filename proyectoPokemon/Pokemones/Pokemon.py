# CLase base Pokemon

class Pokemon():
    def __init__(self, num_pokedex, nombre, peso, sexo, temporada, tipo):
        self.num_pokedex = num_pokedex
        self.nombre = nombre
        self.peso = peso
        self.sexo = sexo
        self.temporada = temporada
        self.tipo = tipo

    def mostrarInformacion(self):
        print(f"Numero Pockemon: {self.num_pokedex}")
        print(f"Nombre: {self.nombre}")
        print(f"Peso: {self.peso}")
        print(f"Sexo: {self.sexo}")
        print(f"Temporada: {self.temporada}")
        print(f"Tipo: {self.tipo}")

    def atacarPlacaje(self):
        print(f"El pokemon '{self.nombre}' de tipo '{self.tipo}' ataca con placaje")

    def atacarAraniazo(self):
        print(f"El pokemon '{self.nombre}' de tipo '{self.tipo}' ataca con araniazo")

    def atacarMordizco(self):
        print(f"El pokemon '{self.nombre}' de tipo '{self.tipo}' ataca con Mordisco")