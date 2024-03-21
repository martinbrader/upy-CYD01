# 21/03/2024 added rotation to initial params, NB defaults to zero
import os

from ili9341 import Display
from machine import ADC, SPI, Pin, SDCard, SoftSPI
from xpt2046 import Touch


class _CydUtils(object):

    def __init__(self, width, height, rotation):
        self._sd_on = False
        self._init_display(width, height, rotation)
        self._init_touchscreen()
        self._init_leds()
        self._init_light_sensor()

    # returns a reference to the CYD display screen
    def cyd_display(self):
        return self._display

    # returns a reference to the CYD touch screen
    def cyd_touch(self, touch_handler):
        self._touch = Touch(
            self._touch_spi, cs=Pin(33), int_pin=Pin(36), int_handler=touch_handler
        )
        return self._touch

    # returns a reference to the CYD light sensor
    def cyd_lightsensor(self):
        return self._lightsensor

    # turn led off
    def led_off(self):
        # turn all off
        self._red_led.value(1)
        self._green_led.value(1)
        self._blue_led.value(1)

    def red_led_on(self):
        self.led_off()
        # turn red on
        self._red_led.value(0)

    def green_led_on(self):
        self.led_off()
        # turn green on
        self._green_led.value(0)

    def blue_led_on(self):
        self.led_off()
        # turn blue on
        self._blue_led.value(0)

    # mount SD card
    def mountSDcard(self):
        if self._sd_on:
            print("SD card already mounted, ignored")
            return True
        try:
            # Set up SD card
            sd = SDCard(slot=2, sck=Pin(18), miso=Pin(19), mosi=Pin(23), cs=Pin(5))
            # Print SD card info (seems to be card size and sector size?)
            print("sd.info", sd.info())

            # Mount SD card and print directory listing
            # SD card must be formatted with a file system recognised by ESP32 (FAT)
            os.mount(sd, "/sd")
            # sd_contents=os.listdir("/sd")
            self._sd_on = True
            return True
        except OSError:
            self._sd_on = False
            print("failed to mount SD card!")
            return False

    def _init_display(self, width, height, rotation):
        # Set up SPI for display
        # Baud rate of 40000000 seems about the max
        self._display_spi = SPI(1, baudrate=40000000, sck=Pin(14), mosi=Pin(13))

        # Set up display
        # The library needs a reset pin, which does not exist on this board
        self._display = Display(
            self._display_spi,
            dc=Pin(2),
            cs=Pin(15),
            rst=Pin(15),
            width=width,
            height=height,
            rotation=rotation,
        )

        # Turn on display backlight
        self._backlight = Pin(21, Pin.OUT)
        self._backlight.on()

    def _init_touchscreen(self):
        # Read touch screen
        # self._touch_spi = SPI(
        #     2, baudrate=1000000, sck=Pin(25), mosi=Pin(32), miso=Pin(39)
        # )
        self._touch_spi = SoftSPI(
            baudrate=100000,
            polarity=1,
            phase=0,
            sck=Pin(25),
            mosi=Pin(32),
            miso=Pin(39),
        )

    def _init_leds(self):
        # RGB LED at the back
        self._red_led = Pin(4, Pin.OUT)
        self._green_led = Pin(16, Pin.OUT)
        self._blue_led = Pin(17, Pin.OUT)
        self.led_off()

    def _init_light_sensor(self):
        self._lightsensor = ADC(34, atten=ADC.ATTN_0DB)


# -----------------------------------
_cyd_utils = None  # used to check only ever one instance of utils


def get_cyd_utils(width=240, height=320, rotation=0):
    global _cyd_utils
    if _cyd_utils is None:
        # cretae an instance
        _cyd_utils = _CydUtils(width, height, rotation)
    return _cyd_utils
