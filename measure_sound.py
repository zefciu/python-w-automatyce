import machine
import utime

detector = machine.Pin(13, machine.Pin.IN)
# diode = machine.Pin(2, machine.Pin.OUT)


def measure(min_time):
    current = detector.value()
    current_ticks = utime.ticks_us()
    # diode_state = 0
    while True:
        value = detector.value()
        if value != current:
            new_ticks = utime.ticks_us()
            elapsed = new_ticks - current_ticks
            if not current and elapsed > min_time:
                print(elapsed)
                # diode_state = int(not diode_state)
                # diode.value(diode_state)
                # print("{}us, {}".format(
                #     elapsed, diode_state
                # ))
            current_ticks = new_ticks
            current = value
