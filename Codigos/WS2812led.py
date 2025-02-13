import array
import time
from machine import Pin
import rp2
import random


# Configurar el número de LEDs WS2812 y el pin
NUM_LEDS = 30
PIN_NUM = 6
brightness = 1

# Definir el programa PIO para enviar datos al LED WS2812
@rp2.asm_pio(sideset_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_LEFT, autopull=True, pull_thresh=24)
def ws2812():
    T1 = 2
    T2 = 5
    T3 = 3
    wrap_target()
    label("bitloop")
    out(x, 1)               .side(0)    [T3 - 1]
    jmp(not_x, "do_zero")   .side(1)    [T1 - 1]
    jmp("bitloop")          .side(1)    [T2 - 1]
    label("do_zero")
    nop()                   .side(0)    [T2 - 1]
    wrap()

# Crear la máquina de estados con el programa PIO ws2812, en el pin especificado
sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(PIN_NUM))

# Iniciar la máquina de estados, quedará esperando datos en su FIFO
sm.active(1)

# Array para almacenar los colores de cada LED
ar = array.array("I", [0 for _ in range(NUM_LEDS)])

##########################################################################
# Función para mostrar los valores actuales en los LEDs
def pixels_show():
    dimmer_ar = array.array("I", [0 for _ in range(NUM_LEDS)])
    for i, c in enumerate(ar):
        r = int(((c >> 8) & 0xFF) * brightness)
        g = int(((c >> 16) & 0xFF) * brightness)
        b = int((c & 0xFF) * brightness)
        dimmer_ar[i] = (g << 16) + (r << 8) + b
    sm.put(dimmer_ar, 8)
    time.sleep_ms(10)

# Función para configurar el color de un LED específico
def pixels_set(i, color):
    ar[i] = (color[1] << 16) + (color[0] << 8) + color[2]

# Función para llenar todos los LEDs con un color
def pixels_fill(color):
    for i in range(len(ar)):
        pixels_set(i, color)

# Función para un efecto de cambio de color en los LEDs
def color_chase(color, wait):
    for i in range(NUM_LEDS):
        pixels_set(i, color)
        time.sleep(wait)
        pixels_show()
    time.sleep(0.2)

# Función para generar un color según posición en la rueda de colores
def wheel(pos):
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

# Función para un ciclo de arcoíris en los LEDs
def rainbow_cycle(wait):
    for j in range(255):
        for i in range(NUM_LEDS):
            rc_index = (i * 256 // NUM_LEDS) + j
            pixels_set(i, wheel(rc_index & 255))
        pixels_show()
        time.sleep(wait)

def color_transition(wait):
    for j in range(255):
        color = wheel(j)
        pixels_fill(color)
        pixels_show()
        time.sleep(wait)
        
def random_twinkle(wait):
    for i in range(NUM_LEDS):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pixels_set(i, color)
    pixels_show()
    time.sleep(wait)
    
def wave_effect(color, wait):
    for i in range(NUM_LEDS * 2):  # La longitud del efecto
        for j in range(NUM_LEDS):
            if (i - j) % 4 == 0:  # Ajusta este valor para el ancho de la onda
                pixels_set(j, color)
            else:
                pixels_set(j, (0, 0, 0))
        pixels_show()
        time.sleep(wait)
        
def color_wave(wait):
    for j in range(255):
        for i in range(NUM_LEDS):
            color = wheel((i * 256 // NUM_LEDS + j) & 255)
            pixels_set(i, color)
        pixels_show()
        time.sleep(wait)
        
def breathing_light(color, steps=50, wait=0.05):
    for intensity in range(steps):
        adjusted_color = (int(color[0] * intensity / steps),
                          int(color[1] * intensity / steps),
                          int(color[2] * intensity / steps))
        pixels_fill(adjusted_color)
        pixels_show()
        time.sleep(wait)
    for intensity in range(steps, -1, -1):
        adjusted_color = (int(color[0] * intensity / steps),
                          int(color[1] * intensity / steps),
                          int(color[2] * intensity / steps))
        pixels_fill(adjusted_color)
        pixels_show()
        time.sleep(wait)

def color_wipe(color, wait):
    for i in range(NUM_LEDS):
        pixels_set(i, color)
        pixels_show()
        time.sleep(wait)
    for i in range(NUM_LEDS):
        pixels_set(i, (0, 0, 0))  # Apaga el LED
        pixels_show()
        time.sleep(wait)

def sparkling_fire(wait):
    for i in range(NUM_LEDS):
        # Colores entre rojo y amarillo
        color = (random.randint(200, 255), random.randint(100, 150), 0)
        pixels_set(i, color)
    pixels_show()
    time.sleep(wait)

def color_trail(color, trail_length=5, wait=0.05):
    for i in range(NUM_LEDS + trail_length):
        for j in range(NUM_LEDS):
            if i - j < trail_length and i - j >= 0:
                brightness_factor = (trail_length - (i - j)) / trail_length
                trail_color = (int(color[0] * brightness_factor),
                               int(color[1] * brightness_factor),
                               int(color[2] * brightness_factor))
                pixels_set(j, trail_color)
            else:
                pixels_set(j, (0, 0, 0))  # Apaga el LED
        pixels_show()
        time.sleep(wait)

def random_flash(wait):
    for i in range(NUM_LEDS):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pixels_set(i, color)
    pixels_show()
    time.sleep(wait)
    pixels_fill((0, 0, 0))  # Apaga todos los LEDs
    pixels_show()

def bounce_back(color, wait):
    for i in range(NUM_LEDS):
        pixels_fill((0, 0, 0))  # Apaga todos los LEDs
        pixels_set(i, color)
        pixels_show()
        time.sleep(wait)
    for i in range(NUM_LEDS - 2, 0, -1):
        pixels_fill((0, 0, 0))
        pixels_set(i, color)
        pixels_show()
        time.sleep(wait)

def color_scanner(color, tail_length=5, wait=0.05):
    for i in range(NUM_LEDS * 2):
        for j in range(NUM_LEDS):
            if abs(i - j) < tail_length:
                brightness_factor = (tail_length - abs(i - j)) / tail_length
                tail_color = (int(color[0] * brightness_factor),
                              int(color[1] * brightness_factor),
                              int(color[2] * brightness_factor))
                pixels_set(j, tail_color)
            else:
                pixels_set(j, (0, 0, 0))  # Apaga el LED
        pixels_show()
        time.sleep(wait)

def meteor_shower(color, decay=0.9, wait=0.05):
    tail_length = 10
    for i in range(NUM_LEDS * 2):
        # Decaer gradualmente el brillo de la tira
        for j in range(NUM_LEDS):
            r = int((ar[j] >> 8) & 0xFF) * decay
            g = int((ar[j] >> 16) & 0xFF) * decay
            b = int((ar[j]) & 0xFF) * decay
            pixels_set(j, (int(g), int(r), int(b)))
        
        # Añade un nuevo "meteoro"
        if i < NUM_LEDS:
            pixels_set(i, color)
        pixels_show()
        time.sleep(wait)

def fading_rainbow(wait):
    for j in range(255):
        color = wheel(j)
        pixels_fill(color)
        pixels_show()
        time.sleep(wait)

def random_sparkles(num_sparkles=10, wait=0.1):
    for _ in range(num_sparkles):
        pixel = random.randint(0, NUM_LEDS - 1)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pixels_set(pixel, color)
        pixels_show()
        time.sleep(wait)
        pixels_set(pixel, (0, 0, 0))  # Apaga el LED
        pixels_show()

def fade_to_black(color, steps=50, wait=0.05):
    for intensity in range(steps, -1, -1):
        dim_color = (int(color[0] * intensity / steps),
                     int(color[1] * intensity / steps),
                     int(color[2] * intensity / steps))
        pixels_fill(dim_color)
        pixels_show()
        time.sleep(wait)

def strobe(color, flashes=10, wait=0.05):
    for _ in range(flashes):
        pixels_fill(color)
        pixels_show()
        time.sleep(wait)
        pixels_fill((0, 0, 0))  # Apaga todos los LEDs
        pixels_show()
        time.sleep(wait)

def knight_rider(color, wait=0.05):
    for i in range(NUM_LEDS * 2):
        pos = i if i < NUM_LEDS else (NUM_LEDS * 2) - i - 1
        pixels_fill((0, 0, 0))  # Apaga todos los LEDs
        pixels_set(pos, color)
        pixels_show()
        time.sleep(wait)

def fade_in_out(color, steps=50, wait=0.02):
    # Desvanece hasta encender
    for i in range(steps):
        adjusted_color = (int(color[0] * i / steps),
                          int(color[1] * i / steps),
                          int(color[2] * i / steps))
        pixels_fill(adjusted_color)
        pixels_show()
        time.sleep(wait)
    # Desvanece hasta apagar
    for i in range(steps, -1, -1):
        adjusted_color = (int(color[0] * i / steps),
                          int(color[1] * i / steps),
                          int(color[2] * i / steps))
        pixels_fill(adjusted_color)
        pixels_show()
        time.sleep(wait)


def alternating_flash(color1, color2, flashes=10, wait=0.2):
    for _ in range(flashes):
        for i in range(NUM_LEDS):
            if i % 2 == 0:
                pixels_set(i, color1)
            else:
                pixels_set(i, color2)
        pixels_show()
        time.sleep(wait)
        
        for i in range(NUM_LEDS):
            if i % 2 == 0:
                pixels_set(i, color2)
            else:
                pixels_set(i, color1)
        pixels_show()
        time.sleep(wait)

def warm_incandescence(wait=0.02):
    # Definir el color incandescente cálido (ajusta la intensidad si lo deseas)
    warm_color = (255, 140, 0)  # Anaranjado cálido estilo bombilla
    steps = 50  # Número de pasos de desvanecimiento

    # Encendido gradual
    for i in range(steps):
        # Ajusta la intensidad del color en función del paso actual
        adjusted_color = (int(warm_color[0] * i / steps),
                          int(warm_color[1] * i / steps),
                          int(warm_color[2] * i / steps))
        pixels_fill(adjusted_color)
        pixels_show()
        time.sleep(wait)
    
    # Mantener encendido durante 5 segundos
    time.sleep(600)
    
    # Apagado gradual
    for i in range(steps, -1, -1):
        adjusted_color = (int(warm_color[0] * i / steps),
                          int(warm_color[1] * i / steps),
                          int(warm_color[2] * i / steps))
        pixels_fill(adjusted_color)
        pixels_show()
        time.sleep(wait)



# Colores básicos para probar en los LEDs
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
COLORS = (BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE)

# # Probar colores individuales
# print("Fills")
# for color in COLORS:       
#     pixels_fill(color)
#     pixels_show()
#     time.sleep(0.2)

# # Efecto de persecución de colores
# print("Chases")
# for color in COLORS:       
#     color_chase(color, 0.01)

# # Ciclo arcoíris
# print("Rainbow")
# rainbow_cycle(0)

# # Ejecuta la secuencia de "color chase"
# print("color chase")
# color_chase((255, 0, 0), 0.05)  # Rojo
# color_chase((0, 255, 0), 0.05)  # Verde
# color_chase((0, 0, 255), 0.05)  # Azul

# # Ejecuta la transición de color
# print("la transición de color")
# color_transition(0.05)

# # Ejecuta el parpadeo aleatorio
# print("aleatorio")
# for _ in range(50):  # Número de parpadeos
#     random_twinkle(0.1)
    
# # Ejecuta la onda de color
# print("efecto ola")
# wave_effect((255, 0, 0), 0.05)  # Rojo
# wave_effect((0, 255, 0), 0.05)  # Verde
# wave_effect((0, 0, 255), 0.05)  # Azul

# # Ejecuta la ola de colores
# print("ola de colores")
# color_wave(0.02)

# # Ejecuta la luz respirable
# print("Luz respirable")
# breathing_light((255, 0, 0))  # Rojo
# breathing_light((0, 255, 0))  # Verde
# breathing_light((0, 0, 255))  # Azul


# # Ejecuta el barrido de color
# print("barrido de color")
# color_wipe((255, 0, 0), 0.05)  # Rojo
# color_wipe((0, 255, 0), 0.05)  # Verde
# color_wipe((0, 0, 255), 0.05)  # Azul


# Ejecuta el efecto de fuego centelleante
print("fuego centelleante")
for _ in range(1000):  # Número de destellos
    sparkling_fire(0.05)


# # Ejecuta el efecto de rastro de color
# print("rastro de color")
# color_trail((255, 0, 0))  # Rojo
# color_trail((0, 255, 0))  # Verde
# color_trail((0, 0, 255))  # Azul

# # Ejecuta el efecto de destello aleatorio
# print("destello aleatorio")
# for _ in range(20):  # Número de flashes
#     random_flash(0.1)


# # Ejecuta el efecto de rebote
# print("efecto de rebote")
# bounce_back((255, 255, 0), 0.05)  # Amarillo

# # Ejecuta el escáner de color
# print("escáner de color")
# color_scanner((0, 255, 255))  # Cyan

# # Ejecuta el efecto de lluvia de meteoros
# print("lluvia de meteoros")
# meteor_shower((255, 100, 0))  # Naranja brillante

# # Ejecuta el efecto de arcoíris degradado
# print("arcoíris degradado")
# fading_rainbow(0.05)

# Ejecuta el efecto de chisporroteo aleatorio
print("chisporroteo aleatorio")
random_sparkles(1000, 0.05)

# # Ejecuta el desvanecimiento a negro
# print("desvanecimiento a negro")
# fade_to_black((0, 0, 255))  # Azul


# # Ejecuta el efecto estroboscópico
# print("efecto estroboscópico")
# strobe((255, 255, 255))  # Blanco brillante


# # Ejecuta el barrido estilo Knight Rider
# print("estilo Knight Rider")
# knight_rider((255, 0, 0))  # Rojo

# Ejecuta el efecto de aparecer y desaparecer
# print(" efecto de aparecer y desaparecer")
# fade_in_out((0, 255, 0))  # Verde

# # Ejecuta el parpadeo alternante
# print(" parpadeo alternante")
# alternating_flash((255, 0, 0), (0, 0, 255))  # Rojo y azul


# Ejecutar el efecto de incandescencia
print("efecto de incandescencia")
warm_incandescence()