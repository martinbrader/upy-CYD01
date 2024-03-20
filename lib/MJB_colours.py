AQUA = const(0x07FF)  # (0, 255, 255)
BLUE = const(0x001F)  # (0, 0, 255)
BLUE_RIBBON = const(0x21F)  # (0, 64, 255)
CHARTREUSE = const(0x87E0)  # (128, 255, 0)
CYAN = const(0x87FF)  # (128, 255, 255)
DARK_BLUE = const(0x401F)  # (64, 0, 255)
DARKGREEN = const(0x0400)  # (0, 128, 0)
DEEP_PINK = const(0xF810)  # (255, 0, 128)
DODGER_BLUE = const(0x041F)  # (0, 128, 255)
FUCHSIA = const(0xF81F)  # (255, 0, 255)
GREEN = const(0x07E0)  # (0, 255, 0)
GREY = const(0x8410)  # (128, 128, 128)
INDIGO = const(0x801F)  # (128, 0, 255)
LIGHT_CORAL = const(0xFC10)  # (255, 128, 128)
LIGHT_GREEN = const(0x87F0)  # (128, 255, 128)
LIGHT_SLATE_BLUE = const(0x841F)  # (128, 128, 255)
LIGHT_YELLOW = const(0xFFF0)  # (255, 255, 128)
MAROON = const(0x8000)  # (128, 0, 0)
NAVY = const(0x0010)  # (0, 0, 128)
OLIVE = const(0x8400)  # (128, 128, 0)
ORANGE = const(0xFC00)  # (255, 128, 0)
PINK = const(0xFC1F)  # (255, 128, 255)
PURPLE = const(0x8010)  # (128, 0, 128)
RED = const(0xF800)  # (255, 0, 0)
SPRING_GREEN = const(0x07F0)  # (0, 255, 128)
TEAL = const(0x0410)  # (0, 128, 128)
WHITE = const(0xFFFF)  # (255, 255, 255)
YELLOW = const(0xFFE0)  # (255, 255, 0)


# use this function to generate the relevant constant
def rgb_to_rgb565(r, g, b):
    return ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)


# here is an example
# r, g, b = 128, 128, 255
# color = rgb_to_rgb565(r, g, b)
# print(hex(color)) # gives 0x841f as output
