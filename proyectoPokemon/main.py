# main.py
from Pokemones.Pokemon import Pokemon
from Pokemones.Bulbasaur import Bulbasaur
from Pokemones.Charmander import Charmander
from Pokemones.Pikachu import Pikachu
from Pokemones.Squirtle import Squirtle

# Creando objetos de cada clase derivada
#               num_pokedex, nombre, peso, sexo, temporada, tipo
pok = Pokemon("011", "Metapod", "10 gr", "S/N", "1er temporada", "Insecto")
bulbasaur = Bulbasaur("4 kg", "S/N")
charmander = Charmander("5 kg", "macho")
pikachu = Pikachu("5 Kg", "S/N")
squirtle = Squirtle("5 kg", "S/N")

# Mostrando información y usando métodos
pok.mostrarInformacion()
pok.atacarPlacaje()
pok.atacarAraniazo()
pok.atacarMordizco()
print("")

bulbasaur.mostrarInformacion()
bulbasaur.atacarParalizar()
bulbasaur.atacarDrenaje()
bulbasaur.atacarHojaAfilada()
bulbasaur.atacarLatigoCepa()
print("")

charmander.mostrarInformacion()
charmander.atacarPunioFuego()
charmander.atacarAscuas()
charmander.atacarLanzaLlamas()
print("")

pikachu.mostrarInformacion()
pikachu.atacarImpactrueno()
pikachu.atacarRayo()
pikachu.atacarImpactrueno()
pikachu.atacarRayoCarga()
print("")

squirtle.mostrarInformacion()
squirtle.atacarHidrobomba()
squirtle.atacarPistolaAgua()
squirtle.atacarBurbuja()
squirtle.atacarHidropulso()
print("")