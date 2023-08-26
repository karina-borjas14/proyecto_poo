from limpiar_pantalla import limpiar_pantalla
from esperar import esperar

class ATM: 
    def iniciar_sesion(self, banco):
        limpiar_pantalla()
        print                   ("╔══════════════════════════════════════════╗")
        print                   ("║         Bienvenido a ImaginBank          ║")
        print                   ("╚══════════════════════════════════════════╝")
        print                   ("╔══════════════════════════════════════════╗")
        numero_tarjeta = input  (" Ingrese el número de tarjeta: ")
        pin = input             (" Ingrese su PIN: ")
        print                   ("╚══════════════════════════════════════════╝")

        if banco.validar_credenciales(numero_tarjeta, pin):
            esperar()
            limpiar_pantalla()
            print("==========¡Inicio de sesión exitoso!==========")
            tarjeta = banco.obtener_tarjeta(numero_tarjeta)
            saldo_actual = tarjeta.obtener_saldo()
            return numero_tarjeta
        else:
            print("Credenciales incorrectas. Por favor, intente nuevamente.")
            esperar()
            return None

    def realizar_operaciones(self, usuario, tarjeta, banco):
        while True:

            print("╔═════════════════════════════════════╗")
            print("║           ELIGE UNA OPCION          ║")
            print("╚═════════════════════════════════════╝")
            print("╔═════════════════════════════════════╗")
            print("║         1. Depositar dinero         ║")
            print("║         2. Retirar dinero           ║")
            print("║         3. Cambiar PIN              ║")
            print("║         4. Revisar saldo            ║")
            print("║         5. Salir                    ║")
            print("╚═════════════════════════════════════╝")
            print("╔═════════════════════════════════════╗")
            opcion = input(" Seleccione una opción: ")
            
            if opcion == "1":
                monto = float(input(" Ingrese el monto a depositar: L."))
                tarjeta.actualizar_saldo(monto)
                banco.actualizar_saldo(tarjeta.numero_tarjeta, monto)  # Actualiza el saldo en la BD cuando hay un deposito
                print(f" Se depositaron L.{monto}. Saldo actual de la cuenta: L.{tarjeta.obtener_saldo()}")
                esperar()
                limpiar_pantalla()
            elif opcion == "2":
                monto = float(input(" Ingrese el monto a retirar: "))
                if monto <= tarjeta.obtener_saldo():
                    tarjeta.actualizar_saldo(-monto)
                    banco.actualizar_saldo(tarjeta.numero_tarjeta, -monto)  # Actualiza el saldo en la BD cuando hay un retiro
                    print(f" Retiraste L.{monto}. Saldo actual de la cuenta: L.{tarjeta.obtener_saldo()}")
                    esperar()
                    limpiar_pantalla()
                else:
                    print(" Saldo insuficiente.")
                    esperar()
                    limpiar_pantalla()
            elif opcion == "3":
                nuevo_pin = input(" Ingrese el nuevo PIN: ")
                usuario.cambiar_pin(nuevo_pin, banco)
                print(" PIN cambiado exitosamente. Por favor, inicie sesión nuevamente.")
                esperar()
                limpiar_pantalla()
                return None  # Termina la sesión actual
            
            elif opcion == "4":
                print(f" Saldo actual: L.{tarjeta.obtener_saldo()}")
                esperar()
                limpiar_pantalla()
            elif opcion == "5":
                limpiar_pantalla()
                print(" ¡Hasta luego!")
                break
            else:
                limpiar_pantalla()
                print(" Opción inválida. Por favor, seleccione una opción válida.")
