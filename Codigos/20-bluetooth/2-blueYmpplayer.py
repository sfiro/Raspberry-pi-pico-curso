# Para que este código de ejemplo funcione, asegúrate de tener una tarjeta SD
# con al menos una carpeta que contenga al menos dos archivos MP3.
# Las carpetas deben estar nombradas como 01, 02, etc., y los archivos deben estar
# nombrados como 001.mp3, 002.mp3, etc.

from machine import Pin, UART  # Importa las clases Pin y UART para manejar pines y comunicación serie
from time import sleep
from picodfplayer import DFPlayer

uart = UART(1, 9600)
# Constantes. Cambia estos valores si el DFPlayer está conectado a otros pines.
UART_INSTANCE = 0
TX_PIN = 16
RX_PIN = 17
BUSY_PIN = 6

# Crear una instancia del reproductor
player = DFPlayer(UART_INSTANCE, TX_PIN, RX_PIN, BUSY_PIN)

led = Pin(25, Pin.OUT)
k = 1
while True:
    # Verifica si el reproductor está ocupado
    if uart.any():
        command = uart.readline()
        command = command.decode("utf-16")
        commands = str(command)
        print(commands)
        if command == '1':
            led.value(1)  # Establece el valor del pin en alto (1)
            sleep(1)
            if player.queryBusy() == False:
                # Reproduce la pista k de la carpeta 1
                player.playTrack(1, 1)
                print("Reproduciendo pista", 1)
                #sleep(60)
                led.value(0)  # Establece el valor del pin en bajo (0)
        
        elif command == '2':
            led.value(1)  # Establece el valor del pin en alto (1)
            sleep(1)
            if player.queryBusy() == False:
                # Reproduce la pista k de la carpeta 1
                player.playTrack(1, 2)
                print("Reproduciendo pista", 2)
                #sleep(3)
                led.value(0)  # Establece el valor del pin en bajo (0)
        
        elif command == '3':
            led.value(1)  # Establece el valor del pin en alto (1)
            sleep(1)
            if player.queryBusy() == False:
                # Reproduce la pista k de la carpeta 1
                player.playTrack(1, 3)
                print("Reproduciendo pista", 3)
                #sleep(3)
                led.value(0)  # Establece el valor del pin en bajo (0)
        
        elif command == '4':
            led.value(1)  # Establece el valor del pin en alto (1)
            sleep(1)
            if player.queryBusy() == False:
                # Reproduce la pista k de la carpeta 1
                player.playTrack(1, 4)
                print("Reproduciendo pista", 4)
                #sleep(3)
                led.value(0)  # Establece el valor del pin en bajo (0)

            


    




