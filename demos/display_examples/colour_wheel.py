import sys
from math import cos, pi, sin

from cyd_colours import rgb_to_rgb565
from cyd_utils import get_cyd_utils
from utime import sleep

HALF_WIDTH = const(120)
HALF_HEIGHT = const(160)
CENTER_X = const(119)
CENTER_Y = const(159)
ANGLE_STEP_SIZE = 0.05  # Decrease step size for higher resolution
PI2 = pi * 2

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


def colour_wheel():
    print("creating colour vectors...")
    x, y = 0, 0
    angle = 0.0
    #  Loop all angles from 0 to 2 * PI radians
    while angle < PI2:
        # Calculate x, y from a vector with known length and angle
        x = int(CENTER_X * sin(angle) + HALF_WIDTH)
        y = int(CENTER_Y * cos(angle) + HALF_HEIGHT)
        colour = rgb_to_rgb565(*hsv_to_rgb(angle / PI2, 1, 1))
        cyd_display.draw_line(x, y, CENTER_X, CENTER_Y, colour)
        angle += ANGLE_STEP_SIZE

    waiting(5)
    print()  # finished

    print("creating coloured circles...")
    for r in range(CENTER_X, 0, -1):
        colour = rgb_to_rgb565(*hsv_to_rgb(r / HALF_WIDTH, 1, 1))
        cyd_display.fill_circle(CENTER_X, CENTER_Y, r, colour)

    waiting(9)
    print()  # finished
    cyd_display.cleanup()


colour_wheel()
print("end of run")
sys.exit()
