from TC import Tarjeta_Credito
class Usuario:
   def __init__(self, nombre, apellido, email):

       self.nombre = nombre

       self.apellido = apellido

       self.email = email

       self.tarjeta = Tarjeta_Credito(0, 20000, 0.015)

usuario1 = Usuario("Benito", "Martinez", "BM@gmail.com")
usuario1.tarjeta.mostrar_info_tarjeta()