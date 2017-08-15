import machine
import utime

detector = machine.Pin(13, machine.Pin.IN)


def measure():
    current_state = detector.value()
    current_ticks = utime.ticks_ms()
    counter = 0
    while True:
        new_state = detector.value()
        if new_state != current_state:
            new_ticks = utime.ticks_ms()
            elapsed = new_ticks - current_ticks
            print('{}: {} {}ms'.format(
                counter,
                'dźwię' if current_state else 'cisza',
                elapsed,
            ))
            current_state = new_state
            current_ticks = new_ticks
            counter += 1
