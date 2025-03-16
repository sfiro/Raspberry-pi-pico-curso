# Controlador del reproductor MP3 DFPlayer utilizando UART para Raspberry Pi Pico.
# Esta librería permite controlar el módulo DFPlayer Mini para reproducir archivos MP3
# almacenados en una tarjeta SD. Proporciona funciones para reproducir, pausar, 
# cambiar de pista, ajustar el volumen, y más.

from machine import UART, Pin
from utime import sleep_ms, sleep

# Constantes

class DFPlayer():
    UART_BAUD_RATE = 9600
    UART_BITS = 8
    UART_PARITY = None
    UART_STOP = 1
    
    START_BYTE = 0x7E
    VERSION_BYTE = 0xFF
    COMMAND_LENGTH = 0x06
    ACKNOWLEDGE = 0x01
    END_BYTE = 0xEF
    COMMAND_LATENCY = 500  # Latencia del comando en milisegundos

    def __init__(self, uartInstance, txPin, rxPin, busyPin):
        """
        Inicializa el DFPlayer con la instancia de UART y los pines especificados.
        
        :param uartInstance: Número de instancia de UART
        :param txPin: Número del pin TX
        :param rxPin: Número del pin RX
        :param busyPin: Número del pin Busy
        """
        self.playerBusy = Pin(busyPin, Pin.IN, Pin.PULL_UP)
        self.uart = UART(uartInstance, baudrate=self.UART_BAUD_RATE, tx=Pin(txPin), rx=Pin(rxPin), bits=self.UART_BITS, parity=self.UART_PARITY, stop=self.UART_STOP)

    def split(self, num):
        """
        Divide un número de 16 bits en dos números de 8 bits.
        
        :param num: Número de 16 bits
        :return: Tupla de dos números de 8 bits
        """
        return num >> 8, num & 0xFF

    def sendcmd(self, command, parameter1, parameter2):
        """
        Envía un comando al DFPlayer.
        
        :param command: Byte de comando
        :param parameter1: Primer byte de parámetro
        :param parameter2: Segundo byte de parámetro
        :return: Respuesta del DFPlayer
        """
        checksum = -(self.VERSION_BYTE + self.COMMAND_LENGTH + command + self.ACKNOWLEDGE + parameter1 + parameter2)
        highByte, lowByte = self.split(checksum)
        toSend = bytes([b & 0xFF for b in [self.START_BYTE, self.VERSION_BYTE, self.COMMAND_LENGTH, command, self.ACKNOWLEDGE, parameter1, parameter2, highByte, lowByte, self.END_BYTE]])

        self.uart.write(toSend)
        sleep_ms(self.COMMAND_LATENCY)
        return self.uart.read()

    def queryBusy(self):
        """
        Consulta el estado de ocupado del DFPlayer.
        
        :return: True si el reproductor está ocupado, False en caso contrario
        """
        return not self.playerBusy.value()
        
    # Comandos comunes de control del DFPlayer
    def nextTrack(self):
        """
        Reproduce la siguiente pista.
        """
        self.sendcmd(0x01, 0x00, 0x00)

    def prevTrack(self):
        """
        Reproduce la pista anterior.
        """
        self.sendcmd(0x02, 0x00, 0x00)

    def increaseVolume(self):
        """
        Aumenta el volumen.
        """
        self.sendcmd(0x04, 0x00, 0x00)

    def decreaseVolume(self):
        """
        Disminuye el volumen.
        """
        self.sendcmd(0x05, 0x00, 0x00)

    def setVolume(self, volume):
        """
        Establece el nivel de volumen.
        
        :param volume: Nivel de volumen (0-30)
        """
        self.sendcmd(0x06, 0x00, volume)

    def setEQ(self, eq):
        """
        Establece el modo del ecualizador.
        
        :param eq: Modo del ecualizador (0: Normal, 1: Pop, 2: Rock, 3: Jazz, 4: Classic, 5: Bass)
        """
        self.sendcmd(0x07, 0x00, eq)

    def setPlaybackMode(self, mode):
        """
        Establece el modo de reproducción.
        
        :param mode: Modo de reproducción (0: Repetir, 1: Repetir carpeta, 2: Repetir una sola, 3: Aleatorio)
        """
        self.sendcmd(0x08, 0x00, mode)

    def setPlaybackSource(self, source):
        """
        Establece la fuente de reproducción.
        
        :param source: Fuente de reproducción (0: U, 1: TF, 2: AUX, 3: SLEEP, 4: FLASH)
        """
        self.sendcmd(0x09, 0x00, source)

    def standby(self):
        """
        Pone el DFPlayer en modo de espera.
        """
        self.sendcmd(0x0A, 0x00, 0x00)

    def normalWorking(self):
        """
        Pone el DFPlayer en modo de trabajo normal.
        """
        self.sendcmd(0x0B, 0x00, 0x00)

    def reset(self):
        """
        Reinicia el DFPlayer.
        """
        self.sendcmd(0x0C, 0x00, 0x00)

    def resume(self):
        """
        Reanuda la reproducción.
        """
        self.sendcmd(0x0D, 0x00, 0x00)

    def pause(self):
        """
        Pausa la reproducción.
        """
        self.sendcmd(0x0E, 0x00, 0x00)

    def playTrack(self, folder, file):
        """
        Reproduce una pista específica de una carpeta.
        
        :param folder: Número de la carpeta
        :param file: Número del archivo
        """
        self.sendcmd(0x0F, folder, file)
                 
    def playMP3(self, filenum):
        """
        Reproduce un archivo MP3 específico.
        
        :param filenum: Número del archivo
        :return: Respuesta del DFPlayer
        """
        a = (filenum >> 8) & 0xff
        b = filenum & 0xff
        return self.sendcmd(0x12, a, b)

    # Consultar parámetros del sistema
    def init(self, params):
        """
        Inicializa el DFPlayer con parámetros específicos.
        
        :param params: Parámetros de inicialización
        """
        self.sendcmd(0x3F, 0x00, params)



