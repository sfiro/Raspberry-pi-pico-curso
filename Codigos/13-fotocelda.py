from machine import Pin, ADC     #importacion de librerias
import time

rojo = Pin(0, Pin.OUT)       #definicion de salida digital GPIO0
verde = Pin(1, Pin.OUT)     #definicion de salida digital GPIO1
azul = Pin(2, Pin.OUT)     #definicion de salida digital GPIO2

foto = ADC(Pin(26))  #definicion de lectura fotocelda


while True:
    lectura = foto.read_u16()    #leer el ADC

    if lectura < 20000 :        # si la lectura es menor de 20000
        rojo.on()
    elif lectura > 10000 and lectura < 30000:   #si la lectura esta entre 10000 y 30000
        verde.on()
    elif lectura > 30000:      #si la lectura es mayor a 30000
        azul.on()
    
    print(lectura)      # se muestra la lectura 
    time.sleep(0.1)     #se espera un pequeño intervalo
    rojo.off()          # se apagan todos los leds
    azul.off()
    verde.off()