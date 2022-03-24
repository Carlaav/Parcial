#Subclases
class Especie:
    def __init__(self, especie):
        self.especie = especie

class Tipo:
    def __init__(self, tipo):
        self.tipo = tipo

class Raza:
    def __init__(self, raza):
        self.raza = raza

#Clase principal porque tiene a todas dentro
class Animal:
    def __init__(self, especie, tipo, raza):
        self.especie = Especie(especie)
        self.tipo = Tipo(tipo)
        self.raza = Raza(raza)
    
    def getEspecie(self):
        return self.especie.especie
    def getTipo(self):
        return self.tipo.tipo
    def getRaza(self):
        return self.raza.raza

animal = Animal("mamifero", "oviparo", "perro")
print(animal.getEspecie())
print(animal.getRaza())
print(animal.getTipo())
