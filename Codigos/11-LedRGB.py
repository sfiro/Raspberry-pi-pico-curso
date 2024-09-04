# Importa las bibliotecas necesarias para controlar temporizadores, pines y PWM
from machine import Pin, PWM
import time

# Configura los pines 0, 1 y 2 como salidas PWM para controlar los LEDs RGB
green = PWM(Pin(0))
blue = PWM(Pin(1))
red = PWM(Pin(2))

tiempo = 0.01

# Función para aumentar el brillo del LED 
def brillo(objeto):
    for pwm in range(0, 65000, 1000):  # Recorre valores de 1000 a 65000 con incrementos de 1000
        objeto.duty_u16(pwm)                 # Establece el ciclo de trabajo del PWM del LED 
        time.sleep(tiempo)                  # Pausa en milisegundos para un aumento gradual del brillo
    
    for pwm in range(65000, 0, -1000):  # Recorre valores de 1000 a 65000 con incrementos de 1000
        objeto.duty_u16(pwm)                 # Establece el ciclo de trabajo del PWM del LED 
        time.sleep(tiempo)                  # Pausa en milisegundos para un aumento gradual del brillo

# Bucle principal que se ejecuta indefinidamente
while True:
    red.duty_u16(0)                 # Establece el ciclo de trabajo del PWM del LED rojo
    green.duty_u16(0)                 # Establece el ciclo de trabajo del PWM del LED rojo
    blue.duty_u16(0)                 # Establece el ciclo de trabajo del PWM del LED rojo

    brillo(red)      # Llama a la función para aumentar el brillo del LED 
    brillo(green)           # Llama a la función para aumentar el brillo del LED 
    brillo(blue)            # Llama a la función para aumentar el brillo del LED