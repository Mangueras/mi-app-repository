from Encapsulamiento import Taco
class Enchilada(Taco):


   def __init__(self, guiso):

       super().__init__(guiso)

       self.salsa = "verde"
  

   def hacer_enchilada(self):

       super().prepararlo()

       print("Agregamos la salsa a nuestro taco y ahora es enchilada")

comer = Enchilada("carne")
comer.hacer_enchilada()