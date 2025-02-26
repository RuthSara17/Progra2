# main.py
from Animales.Animal import Animal
from Animales.Caballo import Caballo
from Animales.Gato import Gato
from Animales.Perro import Perro

# Creando objetos de cada clase derivada
animal = Animal("burro", "negro", "macho")
caballo = Caballo("cafe", "macho", "Arabe", "Golpe de viento")
gato = Gato("plomo", "macho", "Angora", "Mishifu")
perro = Perro("cafe", "macho", "cocker")


# Mostrando información y usando métodos
animal.mostrar_informacion()
animal.correr()
print("")

caballo.mostrar_informacion()
caballo.comer()
print("")

gato.mostrar_informacion()
gato.correr()
print("")

perro.mostrar_informacion()
perro.comer()
print("")