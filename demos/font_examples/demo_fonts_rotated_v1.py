import sys
from time import sleep

from MJB_colours import BLUE, FUCHSIA, GREEN, RED, YELLOW
from MJB_cyd_utils import get_cyd_utils
from xglcd_font import XglcdFont


def waiting(secs):
    for i in range(secs, -1, -1):
        print("\rwaiting for", i, "secs  ", end="")
        sleep(1)
    print("\r", " " * 30, end="")


def fonts_rotated():
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
    print("loading espressodolce")
    espressodolce = XglcdFont("/sd/fonts/EspressoDolce18x24.c", 18, 24)
    print("Loading neato")
    neato = XglcdFont("/sd/fonts/Neato5x7.c", 5, 7, letter_count=223)
    print("Loading robotron")
    robotron = XglcdFont("/sd/fonts/Robotron13x21.c", 13, 21)
    print("Loading unispace")
    unispace = XglcdFont("/sd/fonts/Unispace12x24.c", 12, 24)

    # ArcadePix
    font_height = arcadepix.height
    cyd_display.draw_text(
        0, 0, "Portrait", arcadepix, YELLOW, landscape=False, rotate_180=False
    )
    text_width = arcadepix.measure_text("Landscape")
    cyd_display.draw_text(
        0,
        cyd_display.height - 1,
        "Landscape",
        arcadepix,
        RED,
        landscape=True,
        rotate_180=False,
    )
    text_width = arcadepix.measure_text("Portrait, Rotate 180")
    cyd_display.draw_text(
        cyd_display.width - text_width - 1,
        cyd_display.height - font_height,
        "Portrait, Rotate 180",
        arcadepix,
        FUCHSIA,
        landscape=False,
        rotate_180=True,
    )
    text_width = arcadepix.measure_text("Landscape, Rotate 180")
    cyd_display.draw_text(
        cyd_display.width - font_height - 1,
        text_width,
        "Landscape, Rotate 180",
        arcadepix,
        BLUE,
        landscape=True,
        rotate_180=True,
    )
    waiting(5)

    # Espresso Dolce
    cyd_display.clear()
    font_height = espressodolce.height
    cyd_display.draw_text(
        0, 0, "PORTRAIT", espressodolce, YELLOW, landscape=False, rotate_180=False
    )
    text_width = espressodolce.measure_text("LANDSCAPE")
    cyd_display.draw_text(
        0,
        cyd_display.height - 1,
        "LANDSCAPE",
        espressodolce,
        RED,
        landscape=True,
        rotate_180=False,
    )
    text_width = espressodolce.measure_text("PORTRAIT,")
    cyd_display.draw_text(
        cyd_display.width - text_width - 1,
        cyd_display.height - font_height,
        "PORTRAIT,",
        espressodolce,
        FUCHSIA,
        landscape=False,
        rotate_180=True,
    )
    text_width = espressodolce.measure_text("ROTATE 180")
    cyd_display.draw_text(
        cyd_display.width - text_width - 1,
        cyd_display.height - font_height * 2,
        "ROTATE 180",
        espressodolce,
        FUCHSIA,
        landscape=False,
        rotate_180=True,
    )
    text_width = espressodolce.measure_text("LANDSCAPE,")
    cyd_display.draw_text(
        cyd_display.width - font_height - 1,
        text_width,
        "LANDSCAPE,",
        espressodolce,
        BLUE,
        landscape=True,
        rotate_180=True,
    )
    text_width = espressodolce.measure_text("ROTATE 180")
    cyd_display.draw_text(
        cyd_display.width - font_height * 2 - 1,
        text_width,
        "ROTATE 180",
        espressodolce,
        BLUE,
        landscape=True,
        rotate_180=True,
    )
    waiting(5)

    # Neato
    cyd_display.clear()
    font_height = neato.height
    cyd_display.draw_text(
        0, 0, "Portrait", neato, YELLOW, landscape=False, rotate_180=False
    )
    text_width = neato.measure_text("Landscape")
    cyd_display.draw_text(
        0,
        cyd_display.height - 1,
        "Landscape",
        neato,
        RED,
        landscape=True,
        rotate_180=False,
    )
    text_width = neato.measure_text("Portrait, Rotate 180")
    cyd_display.draw_text(
        cyd_display.width - text_width - 1,
        cyd_display.height - font_height,
        "Portrait, Rotate 180",
        neato,
        FUCHSIA,
        landscape=False,
        rotate_180=True,
    )
    text_width = neato.measure_text("Landscape, Rotate 180")
    cyd_display.draw_text(
        cyd_display.width - font_height - 1,
        text_width,
        "Landscape, Rotate 180",
        neato,
        BLUE,
        landscape=True,
        rotate_180=True,
    )
    waiting(5)

    # Robotron
    cyd_display.clear()
    font_height = robotron.height
    cyd_display.draw_text(
        0, 0, "PORTRAIT", robotron, YELLOW, landscape=False, rotate_180=False
    )
    text_width = robotron.measure_text("LANDSCAPE")
    cyd_display.draw_text(
        0,
        cyd_display.height - 1,
        "LANDSCAPE",
        robotron,
        RED,
        landscape=True,
        rotate_180=False,
    )
    text_width = robotron.measure_text("PORTRAIT,")
    cyd_display.draw_text(
        cyd_display.width - text_width - 1,
        cyd_display.height - font_height,
        "PORTRAIT,",
        robotron,
        FUCHSIA,
        landscape=False,
        rotate_180=True,
    )
    text_width = robotron.measure_text("ROTATE 180")
    cyd_display.draw_text(
        cyd_display.width - text_width - 1,
        cyd_display.height - font_height * 2,
        "ROTATE 180",
        robotron,
        FUCHSIA,
        landscape=False,
        rotate_180=True,
    )
    text_width = robotron.measure_text("LANDSCAPE,")
    cyd_display.draw_text(
        cyd_display.width - font_height - 1,
        text_width,
        "LANDSCAPE,",
        robotron,
        BLUE,
        landscape=True,
        rotate_180=True,
    )
    text_width = robotron.measure_text("ROTATE 180")
    cyd_display.draw_text(
        cyd_display.width - font_height * 2 - 1,
        text_width,
        "ROTATE 180",
        robotron,
        BLUE,
        landscape=True,
        rotate_180=True,
    )
    waiting(5)

    # Unispace
    cyd_display.clear()
    font_height = unispace.height
    cyd_display.draw_text(
        0,
        0,
        "PORTRAIT",
        unispace,
        YELLOW,
        background=RED,
        landscape=False,
        rotate_180=False,
    )
    text_width = unispace.measure_text("LANDSCAPE")
    cyd_display.draw_text(
        0,
        cyd_display.height - 1,
        "LANDSCAPE",
        unispace,
        RED,
        background=YELLOW,
        landscape=True,
        rotate_180=False,
    )
    text_width = unispace.measure_text("PORTRAIT,")
    cyd_display.draw_text(
        cyd_display.width - text_width - 1,
        cyd_display.height - font_height,
        "PORTRAIT,",
        unispace,
        FUCHSIA,
        background=GREEN,
        landscape=False,
        rotate_180=True,
    )
    text_width = unispace.measure_text("ROTATE 180")
    cyd_display.draw_text(
        cyd_display.width - text_width - 1,
        cyd_display.height - font_height * 2,
        "ROTATE 180",
        unispace,
        FUCHSIA,
        background=GREEN,
        landscape=False,
        rotate_180=True,
    )
    text_width = unispace.measure_text("LANDSCAPE,")
    cyd_display.draw_text(
        cyd_display.width - font_height - 1,
        text_width,
        "LANDSCAPE,",
        unispace,
        BLUE,
        background=YELLOW,
        landscape=True,
        rotate_180=True,
    )
    text_width = unispace.measure_text("ROTATE 180")
    cyd_display.draw_text(
        cyd_display.width - font_height * 2 - 1,
        text_width,
        "ROTATE 180",
        unispace,
        BLUE,
        background=YELLOW,
        landscape=True,
        rotate_180=True,
    )

    waiting(10)
    print()  # finished
    cyd_display.cleanup()


fonts_rotated()
print("end of run")
sys.exit()
