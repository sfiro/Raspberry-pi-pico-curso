from machine import Pin   #importar modulos 
import time

rojo = Pin(0, Pin.OUT)     # se configuran los GPIO 0,1,2 como pines de salida digitales
verde = Pin(1, Pin.OUT)
azul = Pin(2, Pin.OUT)

for i in range(5):      # se configura el primer for desde 0 hasta 5 
    rojo.on()
    time.sleep(1)
    rojo.off()
    time.sleep(1)
    print(i)
 
for j in range(5,10):   # se configura el segundo for desde 5 hasta 10
    verde.on()
    time.sleep(1)
    verde.off()
    time.sleep(1)
    print("verde")
    print(j)

for x in range(10,20,2):    # se configura el tercer for desde 10 hasta 20 en pasos de 2 en 2
    azul.on()
    time.sleep(1)
    azul.off()
    time.sleep(1)
    print("azul")
    print(x)