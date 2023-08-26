from usuario import Usuario
from tarjeta import Tarjeta
import sqlite3

class Banco:
    
    #Creamos la conexion a la DB y usamos un try y except en caso de que la DB exista, ésta se actualizará
    #Y en caso de que no exista, la crearemos.
    
    def __init__(self):
        self.conexion = sqlite3.connect('database.db')
        self.cursor = self.conexion.cursor()
        
        try:
            self.cursor.execute('SELECT COUNT(*) FROM usuarios')
            user_count = self.cursor.fetchone()[0]
        except sqlite3.OperationalError:
            self.crear_tablas()
            user_count = 0

        if user_count == 0:
            self.insertar_registros()
    
    def crear_tablas(self):
        self.cursor.execute('''
            CREATE TABLE usuarios (
                numero_tarjeta TEXT PRIMARY KEY,
                pin TEXT
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE tarjetas (
                numero_tarjeta TEXT PRIMARY KEY,
                saldo REAL
            )
        ''')
        self.conexion.commit()
        
#En esta funcion ahora verificara si los registros existen en la BD antes de crear nuevos

    def insertar_registros(self):
        self.cursor.execute('SELECT COUNT(*) FROM usuarios')
        user_count = self.cursor.fetchone()[0]
        if user_count == 0:
            self.cursor.execute('''
                INSERT INTO usuarios (numero_tarjeta, pin) VALUES (?, ?)
            ''', ("123456789", "1234"))

            self.cursor.execute('''
                INSERT INTO tarjetas (numero_tarjeta, saldo) VALUES (?, ?)
            ''', ("123456789", 1000))

            self.conexion.commit()

    def validar_credenciales(self, numero_tarjeta, pin):
        self.cursor.execute('SELECT * FROM usuarios WHERE numero_tarjeta = ? AND pin = ?', (numero_tarjeta, pin))
        return self.cursor.fetchone() is not None

    def obtener_usuario(self, numero_tarjeta):
        self.cursor.execute('SELECT * FROM usuarios WHERE numero_tarjeta = ?', (numero_tarjeta,))
        usuario_data = self.cursor.fetchone()
        if usuario_data:
            return Usuario(usuario_data[0], usuario_data[1])
        return None

    def obtener_tarjeta(self, numero_tarjeta):
        self.cursor.execute('SELECT * FROM tarjetas WHERE numero_tarjeta = ?', (numero_tarjeta,))
        tarjeta_data = self.cursor.fetchone()
        if tarjeta_data:
            return Tarjeta(tarjeta_data[0], tarjeta_data[1])
        return None

    def actualizar_saldo(self, numero_tarjeta, monto):
        self.cursor.execute('UPDATE tarjetas SET saldo = saldo + ? WHERE numero_tarjeta = ?', (monto, numero_tarjeta))
        self.conexion.commit()
    
    def actualizar_pin_en_db(self, numero_tarjeta, nuevo_pin):
        self.cursor.execute('''
            UPDATE usuarios SET pin = ? WHERE numero_tarjeta = ?
        ''', (nuevo_pin, numero_tarjeta))
        self.conexion.commit()

    def __del__(self):
        self.conexion.close()
    

    






