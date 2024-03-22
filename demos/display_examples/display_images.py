import sys

from cyd_utils import get_cyd_utils
from utime import sleep

# get a reference to cyd_utils
cyd_utils = get_cyd_utils()
cyd_display = cyd_utils.cyd_display()

# Set up SD card
if not cyd_utils.mountSDcard():
    print("Abandoned: failed to mount SD card!")
    sys.exit()


def waiting(secs):
    for i in range(secs, -1, -1):
        print("\rwaiting for", i, "secs  ", end="")
        sleep(1)
    print("\r", " " * 30, end="")


def display_images():

    cyd_display.draw_image("/sd/images/RaspberryPiWB128x128.raw", 0, 0, 128, 128)
    waiting(2)

    cyd_display.draw_image("/sd/images/MicroPython128x128.raw", 0, 129, 128, 128)
    waiting(2)

    cyd_display.draw_image("/sd/images/Tabby128x128.raw", 112, 0, 128, 128)
    waiting(2)

    cyd_display.draw_image("/sd/images/Tortie128x128.raw", 112, 129, 128, 128)

    waiting(9)
    print()  # finished
    cyd_display.cleanup()


display_images()
print("end of run")
sys.exit()
