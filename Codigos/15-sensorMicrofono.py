from machine import Pin
import time

# Definición de salidas digitales para los LEDs
rojo = Pin(0, Pin.OUT)
verde = Pin(1, Pin.OUT)
azul = Pin(2, Pin.OUT)

# Definición de entrada digital para la detección
sensor = Pin(16, Pin.IN, Pin.PULL_DOWN)

# Estado inicial de los LEDs
estado_led = 0

while True:
    if sensor.value() == 1:  # Detectar cambio a alto
        estado_led += 1
        if estado_led > 3:
            estado_led = 0
        
        # Controlar los LEDs según el estado
        if estado_led == 1:
            rojo.on()
            verde.off()
            azul.off()
        elif estado_led == 2:
            rojo.off()
            verde.on()
            azul.off()
        elif estado_led == 3:
            rojo.off()
            verde.off()
            azul.on()
        else:
            rojo.off()
            verde.off()
            azul.off()
        
        # Esperar un pequeño intervalo para evitar rebotes
        time.sleep(0.5)
    
    # Pequeño retardo para evitar lecturas continuas
    time.sleep(0.1)