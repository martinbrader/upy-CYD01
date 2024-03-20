import math
import os
import sys

# Simple test to check all functions provided by MJB_cyd_utils are working as expected
# Shows how to use MJB_cyd utils
# Examples based on:
# https://github.com/witnessmenow/ESP32-Cheap-Yellow-Display/blob/main/Examples/Micropython/demo.py
from MJB_colours import BLUE, GREEN, RED, WHITE
from MJB_cyd_utils import get_cyd_utils

# get a reference to cyd_utils
cyd_utils = get_cyd_utils()
cyd_display = cyd_utils.cyd_display()

touch_count = 0  # initialise


# example of function called when touch detected on screen
# prints an X to screen where touch detected
# after every touch cycles through the led switching on red, green, blue alternatively
def touchscreen_press(x, y):
    global touch_count
    global cyd_display
    touch_count += 1
    mod_led = int(math.fmod(touch_count, 3))
    print("Touch at " + str(x) + "," + str(y) + ", " + str(mod_led))
    if mod_led == 1:
        cyd_utils.red_led_on()
        _led = RED
    elif mod_led == 2:
        cyd_utils.green_led_on()
        _led = GREEN
    else:
        cyd_utils.blue_led_on()
        _led = BLUE
    # Y needs to be flipped
    y1 = (cyd_display.height - 1) - y
    cyd_display.draw_text8x8(x, y1, "X", _led)


# get a reference to touch screen and provide a call back routine (touchscreen_press)
cyd_touch = cyd_utils.cyd_touch(touchscreen_press)

# Set up SD card
if not cyd_utils.mountSDcard():
    print("Abandoned: failed to mount SD card!")
    sys.exit()

# print SD directory listing to show SD card available
print(os.listdir("/sd"))

# turn RGB led off
cyd_utils.led_off()

# Read light sensor
print("Read light sensor")
lightsensor = cyd_utils.cyd_lightsensor()
print("Light sendor", lightsensor.read_uv())

cyd_display.draw_text8x8(32, 32, "touch the screen", WHITE)
# loop to wait for touchscreen test
print("press Ctrl-C to exit...")
try:
    while True:
        cyd_touch.get_touch()

except KeyboardInterrupt:
    print("\nCtrl-C pressed.  Cleaning up and exiting...")
finally:
    cyd_display.cleanup()
