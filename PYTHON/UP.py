class Usuario:
    def __init__(self, nombre, apellido, email,):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

    def hacer_compra(self, monto):
        self.saldo_pagar += monto

    def pagar_tarjeta(self, monto):
        self.saldo_pagar -= monto
    def mostrar_saldo_usuario(self):
        print(f"El usuario {self.nombre} {self.apellido}")
        print(f"tiene un nsaldo a pagar de {self.saldo_pagar}")

usuario = Usuario("Benito", "Martinez", "BM@gmail.com")
print(f"El usuario {usuario.nombre} {usuario.apellido} tiene un saldo de {usuario.saldo_pagar}")

usuario.hacer_compra(3.000)
usuario.pagar_tarjeta(1.000)
print(f"El usuario {usuario.nombre} {usuario.apellido} tiene un saldo de {usuario.saldo_pagar}")
usuario.mostrar_saldo_usuario()

