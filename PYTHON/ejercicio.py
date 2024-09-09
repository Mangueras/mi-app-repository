class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0
    
    def hacer_compra(self, monto):
        self.saldo_pagar += monto
        return self
    def pagar_tarjeta(self, monto):
        self.saldo_pagar -= monto
        return self
    def mostrar_saldo_usuario(self):
        print(f"El usuario {self.nombre} {self.apellido}")
        print(f"tiene un saldo a pagar de {self.saldo_pagar}")
        return self
    def transferir_deuda(self, otro_usuario, monto):
        self.saldo_pagar -= monto
        otro_usuario.saldo_pagar += monto
        return self 

usuario4 = Usuario("Jose", "Segundo", "JS@gmail.com")
usuario4.hacer_compra(1500).hacer_compra(1500).pagar_tarjeta(1200)
usuario0 = Usuario("Belen", "Gutierrez", "BG@gmail.com")
usuario0.transferir_deuda(usuario4, 1800)
usuario4.mostrar_saldo_usuario()
usuario0.mostrar_saldo_usuario()

usuario1 = Usuario("Benito", "Martinez", "BM@gmail.com")
usuario2 = Usuario("Jenito", "Nartinez", "JN@gmail.com")
usuario3 = Usuario("Penito", "Ñartinez", "PÑ@gmail.com")
usuario1.hacer_compra(1500).hacer_compra(1500).pagar_tarjeta(1200)
usuario1.mostrar_saldo_usuario()
usuario2.hacer_compra(2000).pagar_tarjeta(600).pagar_tarjeta(600)
usuario2.mostrar_saldo_usuario()
usuario3.hacer_compra(600).hacer_compra(600).hacer_compra(600).pagar_tarjeta(200).pagar_tarjeta(350).pagar_tarjeta(250).pagar_tarjeta(350)
usuario3.mostrar_saldo_usuario( )