from machine import Pin  #importamos la clase Pin del módulo machine, esta nos ayuda a manejar los pines 
import time              #importamos la clase time, esta nos permite manejar el tiempo 

boton = Pin (16,Pin.IN) # se crea el objeto boton en el gpio 16, se define como entrada y se agregan la resistencia de pull UP

while True:            #se define un bucle infinito 
    print(boton.value())   #se lee el valor del pin 16 y se imprime en pantalla 
    time.sleep(0.1)    # se usa el comando sleep para detener un poco la ejecución