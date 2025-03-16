# Para que este código de ejemplo funcione, asegúrate de tener una tarjeta SD
# con al menos una carpeta que contenga al menos dos archivos MP3.
# Las carpetas deben estar nombradas como 01, 02, etc., y los archivos deben estar
# nombrados como 001.mp3, 002.mp3, etc.

from time import sleep
from picodfplayer import DFPlayer

# Constantes. Cambia estos valores si el DFPlayer está conectado a otros pines.
UART_INSTANCE = 0
TX_PIN = 16
RX_PIN = 17
BUSY_PIN = 6

# Crear una instancia del reproductor
player = DFPlayer(UART_INSTANCE, TX_PIN, RX_PIN, BUSY_PIN)

k = 1
while True:
    # Verifica si el reproductor está ocupado
    if player.queryBusy() == False:
        # Reproduce la pista k de la carpeta 1
        player.playTrack(1, k)
        print("Reproduciendo pista", k)
        sleep(5)
        k = k + 1
        # Reinicia k a 1 después de reproducir 4 pistas
        if k == 5:
            k = 1





