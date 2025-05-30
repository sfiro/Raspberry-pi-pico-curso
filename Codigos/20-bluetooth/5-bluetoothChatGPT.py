from machine import UART, Pin
import time

# Inicializar UART1 (TX en GPIO4, RX en GPIO5)
uart1 = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

# Inicializar LED integrado (GPIO 25)
led = Pin(25, Pin.OUT)

# Bucle principal
while True:
    if uart1.any():
        data = uart1.read().decode('utf-8').strip().lower()
        print("Dato recibido:", data)

        if "hola" in data:
            led.value(1)
            uart1.write("LED encendido\n")

        elif "adios" in data:
            led.value(0)
            uart1.write("LED apagado\n")

    time.sleep(0.1)
