# Este programa permite controlar el LED integrado en la Raspberry Pi Pico
# mediante comandos enviados a través de comunicación Bluetooth utilizando UART.
# El LED se enciende o apaga dependiendo del comando recibido.

from machine import Pin, UART  # Importa las clases Pin y UART para manejar pines GPIO y comunicación UART
import utime as time           # Importa la librería utime para manejar tiempos

# Configuración de la comunicación UART
# Se utiliza UART(1) con una velocidad de 9600 baudios para la comunicación Bluetooth
uart = UART(1, 9600)

# Configuración del LED integrado
# El LED integrado está conectado al pin GPIO 25 y configurado como salida digital
led = Pin(25, Pin.OUT)

# Bucle principal
while True:
    # Verifica si hay datos disponibles en el buffer UART
    if uart.any():
        # Lee el comando recibido a través de UART
        command = uart.readline()
        
        # Decodifica el comando desde UTF-16 a una cadena de texto
        command = command.decode("utf-16")
        
        # Convierte el comando a una cadena para facilitar la comparación
        commands = str(command)
        
        # Imprime el comando recibido en la consola
        print(commands)
        
        # Control del LED integrado basado en el comando recibido
        # Si el comando recibido es '9', enciende el LED
        if command == '9':
            led.value(1)  # Establece el valor del pin GPIO 25 en alto (1)
        
        # Si el comando recibido es '7', apaga el LED
        elif command == '7':
            led.value(0)  # Establece el valor del pin GPIO 25 en bajo (0)

