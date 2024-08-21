from machine import Pin, PWM, ADC 
import time

lista =  [ 10 ]   # se crea un listado de valores PWM dentro de una lista

rojo = PWM(Pin(0))    #se define el pin 0 como una salida PWM 

pulsador = Pin(16,Pin.IN,Pin.PULL_UP)   #se define el pulsador como entrada con resistencia de pull up

pot = ADC(Pin(26))  #se define el pin 26 como lectura analoga

while True:
    for dato in lista:   # se crea un for para recorrer la lista 
        rojo.duty_u16(dato)      #enviamos el valor PWM
        print(dato)              # se imprime el dato enviado al PWM
        time.sleep(1)            #esperamos 1 segundo 
    
    if pulsador.value() == 0:    #si es pulsado 
        lectura = pot.read_u16()      #guarda la lectura
        lista.append(lectura)      #la agrega a la lista a recorrer 
        print(lista)        #imprimo la lista

# metodos de List
# append --- agrega el dato al final
# clear  --- borra todos los datos de la lista 
# extend --- agrega una lista a la lista que se le aplica el metodo a la parte final
# count --- cuenta el numero de veces que aparece un termino en una lista
# index --- devuelve el valor del indice donde se encuentre el termino buscado
# insert --- agrega un item a la lista en un indice especifico
# pop  --- elimina el ultimo termino de la lista
# remove --- elimina el primer termino que concuerde con el que indicamos
# reverse --- le da vuelta a la lista actual 
# sort  --- ordena la lista de menor a mayor
        






