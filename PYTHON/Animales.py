class Anmal:
    def __init__(self, nombre, edad, color):
        self.nombre = nombre
        self.edad = edad
        self.color = color

    def hacer_truco(self):
        print(f"{self.nombre} Realizo un truco")

gato = Anmal("Tom", 3, "Blanco")
perro = Anmal("Hashiko", 4, "Negro")

gato.hacer_truco()
perro.hacer_truco()

class gato(Anmal):
    def __init__(self, nombre, edad, color, tipo_pelaje):
        super().__init__(nombre, edad, color,)
        self.tipo_pelaje = tipo_pelaje
    def maullar(self):
        print(f"{self.nombre} Esta maullando")
        return self
    pass

class perro(Anmal):
    def __init__(self, nombre, edad, color, tipo_Raza):
        super().__init__(nombre, edad, color,)
        self.tipo_Raza = tipo_Raza
    def ladrar(self):
        print(f"{self.nombre} Esta ladrando")
        return self
    pass

gato1 = gato("Tom",3,"Cafe","Pelo liso")
gato1.maullar().hacer_truco()

perro1 = perro("Hashiko", 4, "Negro", "Pastor aleman")
perro1.ladrar().hacer_truco()