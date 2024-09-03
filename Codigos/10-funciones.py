# Importa las librerías necesarias para controlar los pines, el ADC, PWM y el tiempo
from machine import Pin, PWM
import time

# Configura los pines 0, 1 y 2 como salidas para controlar los LEDs
rojo = Pin(0, Pin.OUT)
verde = Pin(1, Pin.OUT)
azul = Pin(2, Pin.OUT)

# Configura los pines 16 y 17 como entradas con resistencias pull-up para los pulsadores
pulsador1 = Pin(16, Pin.IN, Pin.PULL_UP)
pulsador2 = Pin(17, Pin.IN, Pin.PULL_UP)

    
def parpadeo(objeto):
    objeto.on()          # Enciende el LED 
    time.sleep(1)       # Espera 1 segundo
    objeto.off()         # Apaga el LED 
    time.sleep(1)       # Espera 1 segundo
    
# Bucle principal que se ejecuta indefinidamente
while True:
    parpadeo(rojo)

    # Si el pulsador 1 está presionado (valor bajo), ejecuta la función para parpadear el LED azul
    if pulsador1.value() == 0:
        parpadeo(azul)
    
    # Si el pulsador 2 está presionado (valor bajo), ejecuta la función para parpadear el LED verde
    if pulsador2.value() == 0:
        parpadeo(verde)