from machine import I2C, Pin
import time

# Configuración I2C en el maestro
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)  # Velocidad a 100 kHz
slave_address = 0x10  # Dirección del esclavo

def send_message(message):
    try:
        i2c.writeto(slave_address, message.encode())
        print("Mensaje enviado:", message)
    except OSError as e:
        print("Error al enviar:", e)

# Prueba enviando los mensajes
while True:
    send_message("hola")  # Enciende el LED
    time.sleep(2)
    send_message("adios")  # Apaga el LED
    time.sleep(2)