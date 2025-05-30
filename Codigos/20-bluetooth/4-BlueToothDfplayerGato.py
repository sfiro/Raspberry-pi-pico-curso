# Para que este código de ejemplo funcione, asegúrate de tener una tarjeta SD
# con al menos una carpeta que contenga al menos dos archivos MP3.
# Las carpetas deben estar nombradas como 01, 02, etc., y los archivos deben estar
# nombrados como 001.mp3, 002.mp3, etc.

from machine import Pin, UART  # Importa las clases Pin y UART para manejar pines y comunicación serie
from time import sleep, ticks_ms, ticks_diff
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

# Variable para controlar el tiempo
last_play_time_ronronear = ticks_ms()  # Marca de tiempo inicial

last_play_time_maullar = ticks_ms()  # Marca de tiempo inicial


# Función para reproducir una pista específica
def play_track(track_number):
    led.value(1)  # Establece el valor del pin en alto (1)
    sleep(1)
    if player.queryBusy() == False:
        player.playTrack(1, track_number)
        sleep(2)
        while player.queryBusy() == True:
            sleep(2)  
            print("Reproduciendo pista", track_number)
            if uart.any(): #si se envia otro dato por bluetooth se detiene la reproduccion
                player.reset()  # Reinicia el reproductor
                print("Reproducción detenida por nuevo comando")
                break
        led.value(0)  # Establece el valor del pin en bajo (0)

sonidoGato = 1
cancion = 7
while True:

    # Verifica si han pasado 1800 segundos - 30 minutos desde la última reproducción automática
    if ticks_diff(ticks_ms(), last_play_time_ronronear) >= 1800000:
        print("Reproducción automática de la pista ronroneo")
        play_track(cancion)  # Reproduce automáticamente la pista 1
        last_play_time_ronronear = ticks_ms()  # Actualiza la marca de tiempo
        cancion = cancion + 1
        if cancion == 11:
            cancion = 7

# Verifica si han pasado 60 segundos desde la última reproducción automática
    if ticks_diff(ticks_ms(), last_play_time_maullar) >= 60000:
        print("Reproducción automática de la pista maullar")
        play_track(sonidoGato)  # Reproduce automáticamente la pista 1
        last_play_time_maullar = ticks_ms()  # Actualiza la marca de tiempo
        sonidoGato = sonidoGato + 1
        if sonidoGato == 7:
            sonidoGato = 1

    # Verifica si el reproductor está ocupado
    if uart.any():
        command = uart.read()
        command = command.decode("utf-16").strip()  #lee todos los datos que ese envian por bluetooth y elimina los espacios en blanco
        commands = str(command)
        print(commands)
        
        if command.isdigit():  # Verifica si el comando es un número
            track_number = int(command)  # Convierte el comando a entero
            play_track(track_number)  # Reproduce la pista correspondiente
        else:
            print("Comando no válido. Debe ser un número.")
        
       
        
     
            


    




