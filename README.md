# upy-CYD01

Cheap Yellow Display examples using micropython

The majority of the examples are modified versions of demos from here:
https://github.com/rdagger/micropython-ili9341/tree/master

## Implementation notes

### SD card

SD card must be formatted with a file system recognised by ESP32 (FAT)

### Touch screen

This is the SPI for the touch screen:
touch_spi = SPI(2, baudrate=1000000, sck=Pin(25), mosi=Pin(32), miso=Pin(39))
to get touch and display working at same time need to use SPI(1, and SPI(2,
but this causes a conflict with SDcard using slot=2
Using SoftSPI for touch appears to resolve this problem!
touch_spi = SoftSPI(baudrate=100000, polarity=1, phase=0, sck=Pin(25), mosi=Pin(32), miso=Pin(39))
touch = Touch(touch_spi, cs=Pin(33), int_pin=Pin(36), int_handler=callback)
