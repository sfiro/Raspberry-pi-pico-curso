from machine import Pin  #importamos la clase Pin del módulo machine, esta nos ayuda a manejar los pines 
import time              #importamos la clase time, esta nos permite manejar el tiempo 

led = Pin(25,Pin.OUT)    # creamos el objeto led, que estará en el Pin 25 y se declara como salida

while True:            #se define un bucle infinito 
    led.on()           #se coloca un estado alto en el pin 25  (se enciende)
    time.sleep(2)      # se espera por 2 segundos
    led.off()          # se coloca un estado bajo en el pin 25 (se apaga)
    time.sleep(2)      # se espera por 2 segundo