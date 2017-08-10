import machine
import utime


MIN_CLAP_TIME = 3
MAX_CLAP_TIME = 7
MAX_BETWEEN_CLAPS = 2e3


DETECTOR = machine.Pin(13, machine.Pin.IN)
LAMP = machine.Pin(12, machine.Pin.OUT)

DEBUG = True


def debug(s):
    if DEBUG:
        print(s)


class ClapDetector(object):

    def __init__(self, detector, callback):
        self.last_clap = None
        self.detector = detector
        self.callback = callback

    def loop(self):
        self.current_state = self.detector.value()
        self.current_ticks = utime.ticks_ms()
        while True:
            new_state = self.detector.value()
            if new_state != self.current_state:
                new_ticks = utime.ticks_ms()
                elapsed = new_ticks - self.current_ticks
                debug("State {} at {}. Elapsed {}".format(
                    new_state, new_ticks, elapsed
                ))
                self.current_state = new_state
                self.current_ticks = new_ticks
                if self.current_state:
                    if MIN_CLAP_TIME < elapsed < MAX_CLAP_TIME:
                        debug("CLAP!")
                        if self.last_clap is not None and (
                            self.current_ticks - self.last_clap <
                            MAX_BETWEEN_CLAPS
                        ):
                            self.callback()
                            self.last_clap = None
                        else:
                            self.last_clap = self.current_ticks


def toggle_lamp():
    debug(LAMP.value())
    LAMP.value(not LAMP.value())


def init():
    detector = ClapDetector(DETECTOR, toggle_lamp)
    detector.loop()
