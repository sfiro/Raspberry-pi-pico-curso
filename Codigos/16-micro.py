from machine import Pin, ADC     #importacion de librerias
import time

foto = ADC(Pin(27))  #definicion de lectura fotocelda

while True:
    lectura = foto.read_u16()    #leer el ADC
    
    print(lectura)      # se muestra la lectura 
    #time.sleep(0.001)     #se espera un pequeño intervalo
   