#programa para el esclavo, este archivo debe llamarse main.py
# Importa las librerías necesarias para la comunicación I2C y el control de los pines
from machine import I2C, Pin
import time

# Inicializa el I2C (I2C0: GP0 y GP1)
i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=100000)

# Dirección del esclavo
slave_address = 0x10

# Configuración del LED en GP16
led = Pin(16, Pin.OUT)

# Búfer para leer mensajes
buffer = bytearray(5)

# Bucle principal
while True:
    # Lee los datos enviados por el maestro
    i2c.readfrom_into(slave_address, buffer)
    message = buffer.decode('utf-8').strip('\x00')
    
    # Verifica el mensaje y controla el LED
    if message == "hola":
        led.on()
        print("LED encendido")
    elif message == "adios":
        led.off()
        print("LED apagado")
    
    time.sleep(0.1)
 