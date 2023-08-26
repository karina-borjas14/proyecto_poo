class Usuario:
    def __init__(self, numero_tarjeta, pin):
        self.numero_tarjeta = numero_tarjeta
        self.pin = pin

    def validar_credenciales(self, numero_tarjeta, pin):
        return self.numero_tarjeta == numero_tarjeta and self.pin == pin
    
    #Actualiza y guarda el cambio del PIN en la DB
    
    def cambiar_pin(self, nuevo_pin, banco):
        self.pin = nuevo_pin
        banco.actualizar_pin_en_db(self.numero_tarjeta, nuevo_pin)