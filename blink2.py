import time
from machine import Pin

diodes = [Pin(x, Pin.OUT) for x in (12, 14, 13)]

def blink():
    counter = 0
    while True:
        diode = diodes[counter % 3]
        diode.value(1)
        time.sleep_ms(500)
        diode.value(0)
        counter += 1
