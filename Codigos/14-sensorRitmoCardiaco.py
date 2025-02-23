from machine import Pin, ADC
import time

# Definición de lectura del sensor de ritmo cardíaco
ritmo = ADC(Pin(26))

# Lista para almacenar las lecturas
lecturas = []
N = 20  # Número de lecturas para la media móvil

while True:
    lectura = ritmo.read_u16()  # leer el ADC
    lecturas.append(lectura)    # agregar la lectura a la lista
    
    if len(lecturas) > N:       # mantener solo las últimas N lecturas
        lecturas.pop(0)

    # Calcular el umbral dinámico
    umbral = (max(lecturas) + min(lecturas)) / 2
    
    # Mostrar la señal filtrada y el umbral dinámico
    print("Señal:", lectura, "Umbral dinámico:", umbral)
   
    time.sleep(0.1)  # pequeño intervalo de tiempo