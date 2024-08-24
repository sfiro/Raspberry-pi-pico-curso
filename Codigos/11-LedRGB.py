# Importa las bibliotecas necesarias para controlar temporizadores, pines y PWM
from machine import Pin, PWM
import time

# Configura los pines 0, 1 y 2 como salidas PWM para controlar los LEDs RGB
green = PWM(Pin(0))
blue = PWM(Pin(1))
red = PWM(Pin(2))

tiempo = 0.1

# Función para aumentar el brillo del LED rojo
def rojo():
    for pwm in range(0, 65000, 1000):  # Recorre valores de 1000 a 65000 con incrementos de 1000
        red.duty_u16(pwm)                 # Establece el ciclo de trabajo del PWM del LED rojo
        time.sleep(tiempo)                  # Pausa de 10 milisegundos para un aumento gradual del brillo
    
    for pwm in range(65000, 0, -1000):  # Recorre valores de 1000 a 65000 con incrementos de 1000
        red.duty_u16(pwm)                 # Establece el ciclo de trabajo del PWM del LED rojo
        time.sleep(tiempo)                  # Pausa de 10 milisegundos para un aumento gradual del brillo

# Función para aumentar el brillo del LED verde
def verde():
    for pwm in range(0, 65000, 1000):  # Recorre valores de 1000 a 65000 con incrementos de 1000
        green.duty_u16(pwm)               # Establece el ciclo de trabajo del PWM del LED verde
        time.sleep(tiempo)                  # Pausa de 10 milisegundos para un aumento gradual del brillo
    
    for pwm in range(65000, 0, -1000):  # Recorre valores de 1000 a 65000 con incrementos de 1000
        green.duty_u16(pwm)               # Establece el ciclo de trabajo del PWM del LED verde
        time.sleep(tiempo)                  # Pausa de 10 milisegundos para un aumento gradual del brillo

# Función para aumentar el brillo del LED azul
def azul():
    for pwm in range(0, 65000, 1000):  # Recorre valores de 1000 a 65000 con incrementos de 1000
        blue.duty_u16(pwm)                # Establece el ciclo de trabajo del PWM del LED azul
        time.sleep(tiempo)                  # Pausa de 10 milisegundos para un aumento gradual del brillo

    for pwm in range(65000, 0, -1000):  # Recorre valores de 1000 a 65000 con incrementos de 1000
        blue.duty_u16(pwm)               # Establece el ciclo de trabajo del PWM del LED verde
        time.sleep(tiempo)                  # Pausa de 10 milisegundos para un aumento gradual del brillo

# Bucle principal que se ejecuta indefinidamente
while True:
    red.duty_u16(0)                 # Establece el ciclo de trabajo del PWM del LED rojo
    green.duty_u16(0)                 # Establece el ciclo de trabajo del PWM del LED rojo
    blue.duty_u16(0)                 # Establece el ciclo de trabajo del PWM del LED rojo
    rojo()            # Llama a la función para aumentar el brillo del LED rojo
    time.sleep(1)     # Pausa de 1 segundo después de completar la secuencia roja
    verde()           # Llama a la función para aumentar el brillo del LED verde
    time.sleep(1)     # Pausa de 1 segundo después de completar la secuencia verde
    azul()            # Llama a la función para aumentar el brillo del LED azul
    time.sleep(1)     # Pausa de 1 segundo después de completar la secuencia azul