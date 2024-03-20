import sys
from time import sleep

from machine import idle
from MJB_colours import CYAN, PURPLE, WHITE
from MJB_cyd_utils import get_cyd_utils
from utime import sleep_us, ticks_diff, ticks_us

# get a reference to cyd_utils
cyd_utils = get_cyd_utils()
cyd_display = cyd_utils.cyd_display()


def waiting(secs):
    for i in range(secs, -1, -1):
        print("\rwaiting for", i, "secs  ", end="")
        sleep(1)
    print("\r", " " * 30, end="")


class Demo(object):
    """Touchscreen simple demo."""

    def __init__(self, display):
        self.display = display
        self.touch = cyd_utils.cyd_touch(self.touchscreen_press)

        # Display initial message
        print("Displaying initial message")

        self.display.draw_text8x8(
            self.display.width // 2 - 32,
            self.display.height - 9,
            "TOUCH ME",
            WHITE,
            background=PURPLE,
        )

        # A small 5x5 sprite for the dot
        self.dot = bytearray(
            b"\x00\x00\x07\xE0\xF8\x00\x07\xE0\x00\x00\x07\xE0\xF8\x00\xF8\x00\xF8\x00\x07\xE0\xF8\x00\xF8\x00\xF8\x00\xF8\x00\xF8\x00\x07\xE0\xF8\x00\xF8\x00\xF8\x00\x07\xE0\x00\x00\x07\xE0\xF8\x00\x07\xE0\x00\x00"
        )
        waiting(5)
        print()
        print("start clicking screen...")

    def touchscreen_press(self, x, y):
        print("touchscreen_press", x, y)
        """Process touchscreen press events."""
        # Y needs to be flipped
        y = (self.display.height - 1) - y
        # Display coordinates
        self.display.draw_text8x8(
            self.display.width // 2 - 32,
            self.display.height - 9,
            "{0:03d}, {1:03d}".format(x, y),
            CYAN,
        )
        # Draw dot
        self.display.draw_sprite(self.dot, x - 2, y - 2, 5, 5)


def touch_demo():
    cyd_display.clear()

    Demo(cyd_display)

    print("press Ctrl-C to exit...")

    try:
        while True:
            idle()

    except KeyboardInterrupt:
        print("\nCtrl-C pressed.  Cleaning up and exiting...")
    finally:
        cyd_display.cleanup()


touch_demo()
print("end of run")
sys.exit()
