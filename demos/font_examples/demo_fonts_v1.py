import sys
from time import sleep

from MJB_colours import (
    AQUA,
    BLUE,
    DARKGREEN,
    DEEP_PINK,
    DODGER_BLUE,
    FUCHSIA,
    GREEN,
    GREY,
    NAVY,
    ORANGE,
    RED,
    WHITE,
    YELLOW,
)
from MJB_cyd_utils import get_cyd_utils
from xglcd_font import XglcdFont


def waiting(secs):
    for i in range(secs, -1, -1):
        print("\rwaiting for", i, "secs  ", end="")
        sleep(1)
    print("\r", " " * 30, end="")


def demo_fonts():
    # get a reference to cyd_utils
    cyd_utils = get_cyd_utils()
    # get ref to cyd display screen
    cyd_display = cyd_utils.cyd_display()
    # Set up SD card
    if not cyd_utils.mountSDcard():
        print("Abandoned: failed to mount SD card!")
        sys.exit()

    print("Loading fonts...")
    print("Loading arcadepix")
    arcadepix = XglcdFont("/sd/fonts/ArcadePix9x11.c", 9, 11)
    print("Loading bally")
    bally = XglcdFont("/sd/fonts/Bally7x9.c", 7, 9)
    print("Loading broadway")
    broadway = XglcdFont("/sd/fonts/Broadway17x15.c", 17, 15)
    print("Loading espresso_dolce")
    espresso_dolce = XglcdFont("/sd/fonts/EspressoDolce18x24.c", 18, 24)
    print("Loading fixed_font")
    fixed_font = XglcdFont("/sd/fonts/FixedFont5x8.c", 5, 8)
    print("Loading neato")
    neato = XglcdFont("/sd/fonts/Neato5x7.c", 5, 7, letter_count=223)
    print("Loading robotron")
    robotron = XglcdFont("/sd/fonts/Robotron13x21.c", 13, 21)
    print("Loading unispace")
    unispace = XglcdFont("/sd/fonts/Unispace12x24.c", 12, 24)
    print("Loading wendy")
    wendy = XglcdFont("/sd/fonts/Wendy7x8.c", 7, 8)
    print("Fonts loaded.")

    cyd_display.draw_text(0, 0, "Arcade Pix 9x11", arcadepix, RED)
    cyd_display.draw_text(0, 22, "Bally 7x9", bally, GREEN)
    cyd_display.draw_text(0, 43, "Broadway 17x15", broadway, BLUE)
    cyd_display.draw_text(0, 66, "Espresso Dolce 18x24", espresso_dolce, AQUA)
    cyd_display.draw_text(0, 104, "Fixed Font 5x8", fixed_font, FUCHSIA)
    cyd_display.draw_text(0, 125, "Neato 5x7", neato, YELLOW)
    cyd_display.draw_text(0, 155, "ROBOTRON 13X21", robotron, WHITE)
    cyd_display.draw_text(0, 190, "Unispace 12x24", unispace, ORANGE)
    cyd_display.draw_text(0, 220, "Wendy 7x8", wendy, DEEP_PINK)

    waiting(9)
    cyd_display.clear()

    cyd_display.draw_text(0, 255, "Arcade Pix 9x11", arcadepix, RED, landscape=True)
    cyd_display.draw_text(22, 255, "Bally 7x9", bally, GREEN, landscape=True)
    cyd_display.draw_text(43, 255, "Broadway 17x15", broadway, BLUE, landscape=True)
    cyd_display.draw_text(
        66,
        255,
        "Espresso Dolce 18x24",
        espresso_dolce,
        AQUA,
        landscape=True,
    )
    cyd_display.draw_text(
        104, 255, "Fixed Font 5x8", fixed_font, FUCHSIA, landscape=True
    )
    cyd_display.draw_text(125, 255, "Neato 5x7", neato, YELLOW, landscape=True)
    cyd_display.draw_text(155, 255, "ROBOTRON 13X21", robotron, WHITE, landscape=True)
    cyd_display.draw_text(190, 255, "Unispace 12x24", unispace, ORANGE, landscape=True)
    cyd_display.draw_text(220, 255, "Wendy 7x8", wendy, DEEP_PINK, landscape=True)

    waiting(9)
    cyd_display.clear()

    cyd_display.draw_text(
        0,
        0,
        "Arcade Pix 9x11",
        arcadepix,
        RED,
        background=AQUA,
    )
    cyd_display.draw_text(0, 22, "Bally 7x9", bally, GREEN, background=NAVY)
    cyd_display.draw_text(
        0,
        43,
        "Broadway",
        broadway,
        BLUE,
        background=YELLOW,
    )
    cyd_display.draw_text(
        0,
        66,
        "Espresso",
        espresso_dolce,
        AQUA,
        background=RED,
    )
    cyd_display.draw_text(
        0,
        104,
        "Fixed Font 5x8",
        fixed_font,
        FUCHSIA,
        background=DARKGREEN,
    )
    cyd_display.draw_text(
        0,
        125,
        "Neato 5x7",
        neato,
        YELLOW,
        background=BLUE,
    )
    cyd_display.draw_text(
        0,
        155,
        "ROBOTRON 13X21",
        robotron,
        WHITE,
        background=GREY,
    )
    cyd_display.draw_text(
        0,
        190,
        "Unispace",
        unispace,
        ORANGE,
        background=DODGER_BLUE,
    )
    cyd_display.draw_text(
        0,
        220,
        "Wendy 7x8",
        wendy,
        DEEP_PINK,
        background=WHITE,
    )

    waiting(9)
    print()  # finished
    cyd_display.cleanup()


demo_fonts()
print("end of run")
sys.exit()
