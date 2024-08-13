from machine import Pin, PWM  # se agregan las clase Pin para manejar puertos y PWM para manejar el pmw en los pines digitales

led = PWM(Pin(16))  # se instancia el objeto led, se crea con la clase PWM y Pin  

while True:
    led.duty_u16(10000) # se envia al pin asociado a led, el ciclo de trabajo determinado  