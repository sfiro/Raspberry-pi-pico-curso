from machine import Pin, ADC  # se agregan las clase Pin para manejar puertos y ADC para manejar el convertidor analogo digital
import time

pot = ADC(Pin(26))  # se instancia el objeto led, se crea con la clase ADC asociada al Pin 26

while True:
    print(pot.read_u16())  # se imprime la lectura analogica del potenciometro 
    time.sleep(0.1)   # se crea un pequeño delay para demorar un poco la ejecución