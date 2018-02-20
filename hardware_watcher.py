import RPi.GPIO as GPIO


class HookedPin:
    def __init__(self, pin, callback):
        self.pin = pin
        self.hooked = False
        self.callback = callback

class ImportWatcher:

    def __init__(self):
        self.hooked_pins = {}


    def hook_gpio(self, hookedPin):
        self.hooked_pins[hookedPin.pin] = hookedPin

    def refresh(self):
        for pin, hookedPin in self.hooked_pins:
            if not hookedPin.hooked:
                GPIO.setup(hookedPin.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                hookedPin.hooked = True

    def watch_pins(self):
        for pin, hookedPin in self.hooked_pins:
            if GPIO.input(hookedPin.pin):
                hookedPin.callback()
