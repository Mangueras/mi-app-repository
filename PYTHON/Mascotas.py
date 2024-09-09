class perro: #Clase
    #Metodo constructor
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad 
perro1 = perro("Hashiko", "Akita", 4)
print(perro1.nombre)
perro1.nombre = "Pelusa"
print(perro1.nombre)

class gato:
    def __init__(self, nombre, raza, color):
        self.name = nombre
        self.raza = raza
        self.color = color 
gato1 = gato("Tom",3, "Blanco")
print(f"{gato1.name} tiene {gato1.raza} años y es de color {gato1.color}")

class perro2:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
    def cumple(self):
        self.age += 1
    def ladrar(self):
        return "Gua Gua"

perro1 = perro("Hashiko", "Akita", 4)
perro1.nombre = "Pelusa"
print(f" {perro1.nombre} dice {perro1.ladrar}")

class gato2:
    def __init__(self, nombre, raza, color):
        self.name = nombre
        self.raza = raza
        self.color = color
    def cumple(self):
        self.edad += 1
    def 