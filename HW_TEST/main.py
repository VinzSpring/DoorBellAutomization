import random

from neopixel import *
import time
import math

from controller import Controller

def state_var(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

@state_var(state=0)
def pulse(f, delta=1):
    pulse.state += delta

    brightness = int(f(pulse.state))
    if brightness >= 255 or brightness <= 0:
        pulse.state = 0
    return brightness


def main():
    controller = Controller(1)

    while True:
        brightness = pulse(lambda x: math.pow(0.7, x)*255)
        controller.setPixelRGB(0, brightness, 0, 0)
        controller.show()
        time.sleep(0.016)


if __name__ == "__main__":
    main()
