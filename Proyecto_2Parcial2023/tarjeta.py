class Tarjeta:
    def __init__(self, numero_tarjeta, saldo):
        self.numero_tarjeta = numero_tarjeta
        self.saldo = saldo

    def obtener_saldo(self):
        return self.saldo

    def actualizar_saldo(self, monto):
        self.saldo += monto