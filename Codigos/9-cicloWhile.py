from machine import Pin
import time
import random       # se importa la libreria random para usar numeros aleatorios

rojo = Pin(0, Pin.OUT)    # se asignan los GPIO de salida 

pulsador = Pin(16,Pin.IN,Pin.PULL_UP)    # se define el pulsado en le GPIO 16 con resistenci de pull up

numero = random.randint(0,1000)    # se crea una variable numero, con un numero aleatorio

while numero > 20 :      #  mientras el numero sea mayor al 20 
    numero = random.randint(0,1000)     # se asigna un valor aleatorio
    print(numero)                       # se imprime la variable
    if pulsador.value() == 0:  
        break

    rojo.on()                         #se enciende el led rojo
    time.sleep(1)
    rojo.off()
    time.sleep(1)

print("Ciclo terminado")