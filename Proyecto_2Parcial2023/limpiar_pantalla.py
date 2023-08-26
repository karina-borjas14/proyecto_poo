import os

def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        print("No se puede limpiar la pantalla en este sistema.")

