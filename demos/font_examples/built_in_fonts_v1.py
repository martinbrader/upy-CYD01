from time import sleep

from MJB_colours import AQUA, BLUE, FUCHSIA, GREEN, RED, WHITE, YELLOW
from MJB_cyd_utils import get_cyd_utils


def run_fonts():
    # get a reference to cyd_utils
    cyd_utils = get_cyd_utils()
    # get ref to cyd display screen
    cyd_display = cyd_utils.cyd_display()

    x_center = cyd_display.width // 2
    y_center = cyd_display.height // 2

    cyd_display.draw_text8x8(0, 0, "Built-in", FUCHSIA)
    cyd_display.draw_text8x8(16, 16, "MicroPython", YELLOW)
    cyd_display.draw_text8x8(32, 32, "8x8 Font", BLUE)

    cyd_display.draw_text8x8(x_center - 40, 120, "Rotate = 0", GREEN)
    cyd_display.draw_text8x8(0, y_center - 44, "Rotate = 90", RED, rotate=90)
    cyd_display.draw_text8x8(
        x_center - 48,
        cyd_display.height - 9,
        "Rotate = 180",
        AQUA,
        rotate=180,
    )
    cyd_display.draw_text8x8(
        cyd_display.width - 9,
        y_center - 48,
        "Rotate = 270",
        WHITE,
        rotate=270,
    )

    cyd_display.draw_text8x8(
        x_center - 40,
        140,
        "Rotate = 0",
        GREEN,
        background=RED,
    )
    cyd_display.draw_text8x8(
        20,
        y_center - 44,
        "Rotate = 90",
        RED,
        rotate=90,
        background=GREEN,
    )
    cyd_display.draw_text8x8(
        x_center - 48,
        cyd_display.height - 29,
        "Rotate = 180",
        AQUA,
        rotate=180,
        background=BLUE,
    )
    cyd_display.draw_text8x8(
        cyd_display.width - 29,
        y_center - 48,
        "Rotate = 270",
        WHITE,
        rotate=270,
        background=FUCHSIA,
    )

    sleep(15)
    cyd_display.cleanup()


run_fonts()
