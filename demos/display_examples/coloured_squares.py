import sys

from MJB_colours import (
    AQUA,
    BLUE,
    CHARTREUSE,
    CYAN,
    DARKGREEN,
    DEEP_PINK,
    DODGER_BLUE,
    FUCHSIA,
    GREEN,
    INDIGO,
    LIGHT_CORAL,
    LIGHT_GREEN,
    LIGHT_SLATE_BLUE,
    LIGHT_YELLOW,
    MAROON,
    NAVY,
    OLIVE,
    ORANGE,
    PINK,
    PURPLE,
    RED,
    SPRING_GREEN,
    TEAL,
    WHITE,
    YELLOW,
)
from MJB_cyd_utils import get_cyd_utils
from utime import sleep

# get a reference to cyd_utils
cyd_utils = get_cyd_utils()
cyd_display = cyd_utils.cyd_display()


def waiting(secs):
    for i in range(secs, -1, -1):
        print("\rwaiting for", i, "secs  ", end="")
        sleep(1)
    print("\r", " " * 30, end="")


def coloured_squares():
    colours = [
        RED,
        GREEN,
        BLUE,
        YELLOW,
        FUCHSIA,
        AQUA,
        MAROON,
        DARKGREEN,
        NAVY,
        TEAL,
        PURPLE,
        OLIVE,
        ORANGE,
        DEEP_PINK,
        CHARTREUSE,
        SPRING_GREEN,
        INDIGO,
        DODGER_BLUE,
        CYAN,
        PINK,
        LIGHT_YELLOW,
        LIGHT_CORAL,
        LIGHT_GREEN,
        LIGHT_SLATE_BLUE,
        WHITE,
    ]
    print("No of colours:", len(colours))
    c = 0
    for y in range(0, 320, 64):
        for x in range(0, 240, 48):
            cyd_display.fill_rectangle(x, y, 47, 63, colours[c])
            c += 1

    waiting(9)
    print()  # finished
    cyd_display.cleanup()


coloured_squares()
print("end of run")
sys.exit()
