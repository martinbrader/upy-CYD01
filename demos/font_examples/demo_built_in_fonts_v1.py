"""ILI9341 demo (fonts 8x8)."""

from time import sleep

from ili9341 import color565
from MJB_cyd import get_cyd_utils


def test():
    """Test code."""
    # get a reference to cyd_utils
    cyd_utils = get_cyd_utils()
    # get ref to cyd display screen
    cyd_display = cyd_utils.cyd_display()

    x_center = cyd_display.width // 2
    y_center = cyd_display.height // 2

    #cyd_display.clear(color565(255, 0, 255))
    cyd_display.draw_text8x8(0, 0, "Built-in", color565(255, 0, 255))
    cyd_display.draw_text8x8(16, 16, "MicroPython", color565(255, 255, 0))
    cyd_display.draw_text8x8(32, 32, "8x8 Font", color565(0, 0, 255))

    cyd_display.draw_text8x8(x_center - 40, 120, "Rotate = 0", color565(0, 255, 0))
    cyd_display.draw_text8x8(
        0, y_center - 44, "Rotate = 90", color565(255, 0, 0), rotate=90
    )
    cyd_display.draw_text8x8(
        x_center - 48,
        cyd_display.height - 9,
        "Rotate = 180",
        color565(0, 255, 255),
        rotate=180,
    )
    cyd_display.draw_text8x8(
        cyd_display.width - 9,
        y_center - 48,
        "Rotate = 270",
        color565(255, 255, 255),
        rotate=270,
    )

    cyd_display.draw_text8x8(
        x_center - 40,
        140,
        "Rotate = 0",
        color565(0, 255, 0),
        background=color565(255, 0, 0),
    )
    cyd_display.draw_text8x8(
        20,
        y_center - 44,
        "Rotate = 90",
        color565(255, 0, 0),
        rotate=90,
        background=color565(0, 255, 0),
    )
    cyd_display.draw_text8x8(
        x_center - 48,
        cyd_display.height - 29,
        "Rotate = 180",
        color565(0, 255, 255),
        rotate=180,
        background=color565(0, 0, 255),
    )
    cyd_display.draw_text8x8(
        cyd_display.width - 29,
        y_center - 48,
        "Rotate = 270",
        color565(255, 255, 255),
        rotate=270,
        background=color565(255, 0, 255),
    )

    # sleep(15)
    sleep(5)
    cyd_display.cleanup()


test()
