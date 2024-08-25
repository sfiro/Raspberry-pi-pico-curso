# Importa las bibliotecas necesarias para controlar temporizadores, pines y PWM
from machine import Pin, PWM
from math import sin, cos, pi
import time


# Configura los pines 0, 1 y 2 como salidas PWM para controlar los LEDs RGB
green = PWM(Pin(0))
blue = PWM(Pin(1))
red = PWM(Pin(2))

rad = 0  #variable para radianes

# Bucle principal que se ejecuta indefinidamente
while True:
 
    seno = int((((sin(rad))/2)+0.5)*65535)        #función seno escalada
    seno2 = int((((sin(rad+ pi))/2)+0.5)*65535)   #función seno desplazada 180 grados
    coseno = int((((cos(rad))/2)+0.5)*65535)     #funcion coseno escalada o funcion seno desplazada 90 grados 

    red.duty_u16(seno)                 # Establece el ciclo de trabajo del PWM del LED rojo
    green.duty_u16(coseno)               # Establece el ciclo de trabajo del PWM del LED verde    
    blue.duty_u16(seno2)               # Establece el ciclo de trabajo del PWM del LED verde    
    
    print(seno,coseno,seno2)      # se imprimen las variables 

    rad = rad + 0.2     #pasos de la variable rad
    time.sleep(0.1)