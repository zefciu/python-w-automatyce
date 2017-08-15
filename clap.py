import machine
import utime


CLAP_DELAY = 300
SILENCE_AFTER_CLAP = 150
MAX_BETWEEN_CLAPS = 2000


DETECTOR = machine.Pin(13, machine.Pin.IN)
LAMP = machine.Pin(12, machine.Pin.OUT)
LAMP.off()

DEBUG = True


def debug(s):
    if DEBUG:
        print(s)


class ClapDetector(object):

    def __init__(self, detector, callback):
        self.last_clap = None
        self.callback = callback

    def expect_silence(self, length):
        start_time = utime.ticks_ms()
        debug('START: {}'.format(start_time))
        while utime.ticks_ms() < start_time + length:
            if not DETECTOR.value():
                debug('BREAK: {}'.format(utime.ticks_ms()))
                return False
        return True

    def loop(self):
        self.current_ticks = utime.ticks_ms()
        while True:
            new_state = DETECTOR.value()
            if new_state == 1:
                continue
            utime.sleep_ms(CLAP_DELAY)
            if not self.expect_silence(SILENCE_AFTER_CLAP):
                continue
            self.register_clap(utime.ticks_ms())

    def register_clap(self, ticks):
        debug('CLAP')
        if self.last_clap and ticks - self.last_clap < MAX_BETWEEN_CLAPS:
            self.callback()
        else:
            self.last_clap = ticks


counter = 0


def clap():
    global counter
    debug("CLAP! CLAP! {}".format(counter))
    counter += 1
    LAMP.value(0 if LAMP.value() else 1)


def init():
    detector = ClapDetector(DETECTOR, clap)
    detector.loop()
