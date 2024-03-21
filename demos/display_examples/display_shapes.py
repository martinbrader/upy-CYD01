import sys

from MJB_colours import (
    AQUA,
    BLUE,
    BLUE_RIBBON,
    DARK_BLUE,
    FUCHSIA,
    GREEN,
    INDIGO,
    LIGHT_SLATE_BLUE,
    RED,
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


def display_shapes():

    cyd_display.clear(DARK_BLUE)
    waiting(1)

    cyd_display.clear()

    cyd_display.draw_hline(10, 319, 229, FUCHSIA)
    waiting(1)

    cyd_display.draw_vline(10, 0, 319, AQUA)
    waiting(1)

    cyd_display.fill_hrect(23, 50, 30, 75, WHITE)
    waiting(1)

    cyd_display.draw_hline(0, 0, 222, RED)
    waiting(1)

    cyd_display.draw_line(127, 0, 64, 127, YELLOW)
    waiting(2)

    cyd_display.clear()

    coords = [[0, 63], [78, 80], [122, 92], [50, 50], [78, 15], [0, 63]]
    cyd_display.draw_lines(coords, AQUA)
    waiting(1)

    cyd_display.clear()
    cyd_display.fill_polygon(7, 120, 120, 100, GREEN)
    waiting(1)

    cyd_display.fill_rectangle(0, 0, 15, 227, RED)
    waiting(1)

    cyd_display.clear()

    cyd_display.fill_rectangle(0, 0, 163, 163, LIGHT_SLATE_BLUE)
    waiting(1)

    cyd_display.draw_rectangle(0, 64, 163, 163, FUCHSIA)
    waiting(1)

    cyd_display.fill_rectangle(64, 0, 163, 163, INDIGO)
    waiting(1)

    cyd_display.draw_polygon(3, 120, 286, 30, BLUE_RIBBON, rotate=15)
    waiting(3)

    cyd_display.clear()

    cyd_display.fill_circle(132, 132, 70, GREEN)
    waiting(1)

    cyd_display.draw_circle(132, 96, 70, BLUE)
    waiting(1)

    cyd_display.fill_ellipse(96, 96, 30, 16, RED)
    waiting(1)

    cyd_display.draw_ellipse(96, 256, 16, 30, YELLOW)

    waiting(5)
    print()  # finished
    cyd_display.cleanup()


display_shapes()
print("end of run")
sys.exit()
