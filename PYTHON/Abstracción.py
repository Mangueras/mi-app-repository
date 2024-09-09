from Encapsulamiento import Taco
class Comensal:

   def __init__(self, nombre):

       self.nombre = nombre

       self.taco = Taco("carne")
  

   def comer_taco(self):

       self.taco.prepararlo()

       self.taco.servir()

       print("Me como mi delicioso taco")