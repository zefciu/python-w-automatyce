import time
from machine import Pin

diode = Pin(13, Pin.OUT)

def blink():
    while True:
        diode.value(0 if diode.value() else 1)
        time.sleep_ms(500)
