class Tarjeta_Credito:
    def __init__(self, saldo_pagar, limite_credito, intereses):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses
        self.saldo_disponible = limite_credito - saldo_pagar

    def compra(self, monto):
        if monto > self.saldo_disponible:
            print("No tiene saldo suficiente")
            return self
        else:
            self.saldo_pagar += monto
            self.saldo_disponible = self.limite_credito - self.saldo_pagar
            print(f"La compra se realizo, su saldo disponible es: {self.saldo_disponible}")
            return self

    def pago(self, monto):
        if monto > self.saldo_pagar:
            print("El pago es demas a la deuda")
            return self
        else:
            self.saldo_pagar -= monto
            self.saldo_disponible = self.limite_credito - self.saldo_pagar
            print(f"El pago se realizo, su saldo disponible es: {self.saldo_disponible}")
            return self

    def mostrar_info_tarjeta(self):
        print(f"Saldo a pagar: {self.saldo_pagar}")
        print(f"Saldo disponible: {self.saldo_disponible}")
        print(f"Limite de credito: {self.limite_credito}")
        return self

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        self.saldo_disponible = self.limite_credito - self.saldo_pagar
        print(f"Intereses cobrados, saldo disponible {self.saldo_disponible}")
        return self

#t1 =Tarjeta_Credito(0,20000,0.01)
#t2 =Tarjeta_Credito(0,30000,0.01)
#t3 =Tarjeta_Credito(0,50000,0.01)

#t1.compra(1000).compra(1500).pago(2250).cobrar_interes().mostrar_info_tarjeta()
#t2.compra(1500).compra(3500).compra(2000).pago(2000).pago(3000).cobrar_interes().mostrar_info_tarjeta()
#t3.compra(15000).compra(10000).compra(10000).compra(10000).compra(10000).mostrar_info_tarjeta()