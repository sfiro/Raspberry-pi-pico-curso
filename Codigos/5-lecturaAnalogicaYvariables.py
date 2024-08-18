from machine import Pin, ADC  # se agregan las clase Pin para manejar puertos y ADC para manejar el convertidor analogo digital
import time

pot = ADC(Pin(26))  # se instancia el objeto led, se crea con la clase ADC asociada al Pin 26
g_vol =3.3/65535    # ganancia ADC de voltaje


while True:
    lectura = pot.read_u16()     #lectura de potenciometro  valor entre 0 - 65535
    voltaje = lectura * g_vol    #lectura convertida a voltios entre 0 V - 3.3 V
    print(voltaje)  # se imprime la lectura analogica del potenciometro 
    time.sleep(0.1)   # se crea un pequeño delay para demorar un poco la ejecución