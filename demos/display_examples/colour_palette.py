import sys
from time import sleep

from MJB_colours import rgb_to_rgb565
from MJB_cyd_utils import get_cyd_utils

# get a reference to cyd_utils
cyd_utils = get_cyd_utils()
cyd_display = cyd_utils.cyd_display()


def waiting(secs):
    for i in range(secs, -1, -1):
        print("\rwaiting for", i, "secs  ", end="")
        sleep(1)
    print("\r", " " * 30, end="")


def hsv_to_rgb(h, s, v):
    """
    Convert HSV to RGB (based on colorsys.py).

        Args:
            h (float): Hue 0 to 1.
            s (float): Saturation 0 to 1.
            v (float): Value 0 to 1 (Brightness).
    """
    if s == 0.0:
        return v, v, v
    i = int(h * 6.0)
    f = (h * 6.0) - i
    p = v * (1.0 - s)
    q = v * (1.0 - s * f)
    t = v * (1.0 - s * (1.0 - f))
    i = i % 6

    v = int(v * 255)
    t = int(t * 255)
    p = int(p * 255)
    q = int(q * 255)

    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    if i == 5:
        return v, p, q


def colour_palette():
    c = 0
    for x in range(0, 240, 20):
        for y in range(0, 320, 20):
            color = rgb_to_rgb565(*hsv_to_rgb(c / 192, 1, 1))
            cyd_display.fill_circle(x + 9, y + 9, 9, color)
            c += 1
    waiting(9)
    print()  # finished
    cyd_display.cleanup()


colour_palette()
print("end of run")
sys.exit()
