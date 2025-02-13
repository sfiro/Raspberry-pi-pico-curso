from machine import Pin, ADC     #importacion de librerias
import time

rojo = Pin(0, Pin.OUT)       #definicion de salida digital GPIO0
verde = Pin(1, Pin.OUT)     #definicion de salida digital GPIO1
azul = Pin(2, Pin.OUT)     #definicion de salida digital GPIO2

ritmo = ADC(Pin(26))  #definicion de lectura ritmo cardiaco

while True:
    lectura = ritmo.read_u16()    #leer el ADC
    lectura = lectura - 25000
    lectura = lectura * 2
    if lectura < 0 :        # si la lectura es menor de 20000
        lectura = 0
    
    if lectura > 25000:
        lectura = 25000
    

    
    print(lectura)      # se muestra la lectura 
    time.sleep(0.1)     #se espera un pequeño intervalo
    rojo.off()          # se apagan todos los leds
    azul.off()
    verde.off()