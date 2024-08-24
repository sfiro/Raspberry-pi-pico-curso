# Importa las librerías necesarias para controlar los pines, el ADC, PWM y el tiempo
from machine import Pin, PWM
import time
import random

# Configura los pines 0, 1 y 2 como salidas para controlar los LEDs
rojo = Pin(0, Pin.OUT)
verde = Pin(1, Pin.OUT)
azul = Pin(2, Pin.OUT)

# Configura los pines 16 y 17 como entradas con resistencias pull-up para los pulsadores
pulsador1 = Pin(16, Pin.IN, Pin.PULL_UP)
pulsador2 = Pin(17, Pin.IN, Pin.PULL_UP)

# Función para hacer parpadear el LED azul
def parpadeoAzul():
    azul.on()           # Enciende el LED azul
    time.sleep(1)       # Espera 1 segundo
    azul.off()          # Apaga el LED azul
    time.sleep(1)       # Espera 1 segundo

# Función para hacer parpadear el LED verde
def parpadeoVerde():
    verde.on()          # Enciende el LED verde
    time.sleep(1)       # Espera 1 segundo
    verde.off()         # Apaga el LED verde
    time.sleep(1)       # Espera 1 segundo

# Bucle principal que se ejecuta indefinidamente
while True:
    rojo.on()           # Enciende el LED rojo
    time.sleep(1)       # Espera 1 segundo
    rojo.off()          # Apaga el LED rojo
    time.sleep(1)       # Espera 1 segundo

    # Si el pulsador 1 está presionado (valor bajo), ejecuta la función para parpadear el LED azul
    if pulsador1.value() == 0:
        parpadeoAzul()
    
    # Si el pulsador 2 está presionado (valor bajo), ejecuta la función para parpadear el LED verde
    if pulsador2.value() == 0:
        parpadeoVerde()