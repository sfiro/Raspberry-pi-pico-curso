from machine import I2C, Pin
from Servo import Servos
import time

sda = Pin(0)
scl = Pin(1)
i2c = I2C(0, sda=Pin(0), scl=Pin(1))

servo = Servos(i2c=i2c)

while(True):
    servo.position(index=0, degrees=0)
    time.sleep(1)
    servo.position(index=0, degrees=180)
    time.sleep(1)
    servo.position(index=1, degrees=0)
    time.sleep(1)
    servo.position(index=1, degrees=180)
    time.sleep(1)
    servo.position(index=2, degrees=0)
    time.sleep(1)
    servo.position(index=2, degrees=180)
    time.sleep(1)
    servo.position(index=3, degrees=0)
    time.sleep(1)
    servo.position(index=3, degrees=180)
    time.sleep(1)
    servo.position(index=4, degrees=0)
    time.sleep(1)
    servo.position(index=4, degrees=180)
    time.sleep(1)
    servo.position(index=5, degrees=0)
    time.sleep(1)
    servo.position(index=5, degrees=180)
    time.sleep(1)