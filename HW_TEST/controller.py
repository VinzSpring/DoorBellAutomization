from neopixel import *
import rpi_ws281x as ws

__all__ = ['Controller']


class Controller(object):

    # LED strip configuration:
    LED_COUNT = 1  # Number of LED pixels.
    LED_PIN = 19  # GPIO pin connected to the pixels (18 uses PWM!).
    # LED_PINstrip        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
    LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA = 5  # DMA channel to use for generating signal (try 5)
    LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
    LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
    LED_CHANNEL = 1  # set to '1' for GPIOs 13, 19, 41, 45 or 53
    LED_STRIP = ws.WS2812_STRIP  # Strip type and colour ordering

    # Var for strip instance
    STRIP = None

    # Constructor
    def __init__(self, numberLED):
        # Set count of LEDs
        self.LED_COUNT = numberLED

        # Initialize strip object
        self.STRIP = Adafruit_NeoPixel(self.LED_COUNT,
                                       self.LED_PIN,
                                       self.LED_FREQ_HZ,
                                       self.LED_DMA,
                                       self.LED_INVERT,
                                       self.LED_BRIGHTNESS,
                                       self.LED_CHANNEL,
                                       self.LED_STRIP)

        # Start LED control
        self.STRIP.begin()

    def setPixelRGB(self, pixel, r, g, b):
        self.STRIP.setPixelColorRGB(pixel, r, g, b)

    def show(self):
        self.STRIP.show()
