import RPi.GPIO as GPIO


class HookedPin:
    def __init__(self, pin, callback):
        self.pin = pin
        self.hooked = False
        self.callback = callback

    def send(self, delay):
        pass


class ImportWatcher:

    def __init__(self):
        self.hooked_pins = {}

    def hook_gpio(self, hooked_pin):
        self.hooked_pins[hooked_pin.pin] = hooked_pin

    def refresh(self):
        for pin, hookedPin in self.hooked_pins:
            if not hookedPin.hooked:
                GPIO.setup(hookedPin.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
                hookedPin.hooked = True

    def watch_pins(self):
        for pin, hookedPin in self.hooked_pins:
            if GPIO.input(hookedPin.pin):
                hookedPin.callback()

    def send_to_pin(self, pin, delay):
        self.hooked_pins[pin].send(delay)
        pass
