from machine import Pin, UART
import utime
from dfplayer import DFPlayerMini

# Configuración de los pines y la UART
TX_PIN = Pin(0)  # Conectar a RX del DFPlayer
RX_PIN = Pin(1)  # Conectar a TX del DFPlayer
UART_ID = 0  # UART 0 para Raspberry Pi Pico

# Inicializar el módulo DFPlayer Mini
dfplayer = DFPlayerMini(UART_ID, TX_PIN, RX_PIN)

# Reiniciar el módulo
dfplayer.send_command(0x0C, 0x00, 0x00)  # Comando reset
utime.sleep(2)

# Configuración inicial
dfplayer.set_volume(20)            # Establece el volumen
dfplayer.set_EQ("normal")           # Establece el ecualizador a 'normal'
dfplayer.set_output_device("sd")    # Selecciona la tarjeta SD como salida

# Reproduce la primera canción de la carpeta 01
dfplayer.play_track(1, 1)
print("Reproduciendo canción 001 de la carpeta 01")

# Bucle principal
while True:
    if dfplayer.is_playing():
        print("Reproducción en curso...")
    else:
        print("No se está reproduciendo ninguna canción.")
        # Aquí podrías iniciar la siguiente canción
    utime.sleep(5)