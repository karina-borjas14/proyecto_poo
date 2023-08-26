from atm import ATM
from banco import Banco

# Creacion de las instancias de las clases
banco = Banco()
atm = ATM()

bandera= None
while bandera is None:

    # Iniciar sesión
    numero_tarjeta = None
    while numero_tarjeta is None:
        numero_tarjeta = atm.iniciar_sesion(banco)
        
        if numero_tarjeta:
            usuario = banco.obtener_usuario(numero_tarjeta)
            tarjeta = banco.obtener_tarjeta(numero_tarjeta)
            atm.realizar_operaciones(usuario, tarjeta, banco)

            