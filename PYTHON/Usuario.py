from TC import Tarjeta_Credito

class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.tarjeta = []

    def agregar_tarjeta(self, saldo_pagar, limite_credito, intereses):
        tarjeta = Tarjeta_Credito(saldo_pagar, limite_credito, intereses)
        self.tarjeta.append(tarjeta)

    def hacer_compra(self, monto):
        self.tarjeta[-1].compra(monto)

    def pagar_tarjeta(self, monto):
        self.tarjeta[-1].pago(monto)

    def mostrar_saldo_usuario(self):
        print(self.tarjeta[-1].saldo_disponible)

if __name__ == "__main__":
    Usuario1 = Usuario("Alberto", "Vicenció", "AV@gmail.com")
    Usuario1.agregar_tarjeta(saldo_pagar=0, limite_credito=30000, intereses=0.01)
    Usuario1.hacer_compra(1500)
    Usuario1.pagar_tarjeta(1200)
    Usuario1.mostrar_saldo_usuario()
