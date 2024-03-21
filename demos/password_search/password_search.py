"""Search online for pwned passwords."""

import gc
import sys
from hashlib import sha1

from MJB_colours import BLUE, GREEN, RED, WHITE
from MJB_cyd_utils import get_cyd_utils
from MJB_wifi_manager import WifiManager
from password_search.urequests2 import get
from ubinascii import hexlify
from utime import sleep
from xglcd_font import XglcdFont

from demos.password_search.MJB_touch_keyboard import TouchKeyboard


class PwnLookup(object):
    """Checks if password is pwned."""

    def __init__(self, wlan, cyd_utils):
        self.wlan = wlan
        # get ref to cyd display screen
        self.cyd_display = cyd_utils.cyd_display()

        # Set up touchscreen
        self.xpt = cyd_utils.cyd_touch(self.touchscreen_press)

        # Load font
        self.unispace = XglcdFont("/sd/fonts/Unispace12x24.c", 12, 24)

        # Set up Keyboard
        self.keyboard = TouchKeyboard(self.cyd_display, self.unispace)

    def lookup(self, pwd):
        """Return the number of times password found in pwned database.

        Args:
            pwd: password to check
        Returns:
            integer: password hits from online pwned database.
        Raises:
            IOError: if there was an error due to WiFi network.
            RuntimeError: if there was an error trying to fetch data from dB.
            UnicodeError: if there was an error UTF_encoding the password.
        """
        sha1pwd = sha1(pwd.encode("utf-8")).digest()
        sha1pwd = hexlify(sha1pwd).upper().decode("utf-8")
        head, tail = sha1pwd[:5], sha1pwd[5:]

        if not self.wlan.isconnected():
            raise IOError("WiFi network error")

        hits = 0
        gc.collect()
        with get("https://api.pwnedpasswords.com/range/" + head) as response:
            for line in response.iter_lines():
                l = line.decode(response.encoding).split(":")
                if l[0] == tail:
                    hits = int(l[1])
                    break
        gc.collect()

        return hits

    def touchscreen_press(self, x, y):
        """Process touchscreen press events."""
        if self.keyboard.handle_keypress(x, y, debug=False) is True:
            self.keyboard.locked = True
            pwd = self.keyboard.kb_text

            self.keyboard.show_message("Searching...", BLUE)
            try:
                hits = self.lookup(pwd)

                if hits:
                    # Password found
                    msg = "PASSWORD HITS: {0}".format(hits)
                    self.keyboard.show_message(msg, RED)
                else:
                    # Password not found
                    msg = "PASSWORD NOT FOUND"
                    self.keyboard.show_message(msg, GREEN)
            except Exception as e:
                if hasattr(e, "message"):
                    self.keyboard.show_message(e.message[:22], WHITE)
                else:
                    self.keyboard.show_message(str(e)[:22], WHITE)

            self.keyboard.waiting = True
            self.keyboard.locked = False


def password_lookup():
    # get a reference to cyd_utils
    cyd_utils = get_cyd_utils(rotation=270)
    # Set up SD card
    if not cyd_utils.mountSDcard():
        print("Abandoned: failed to mount SD card!")
        sys.exit()

    wm = WifiManager()
    wm.connect()
    try:
        print("press Ctrl-C to exit...")
        while True:
            if wm.is_connected():
                PwnLookup(wm, cyd_utils)
            else:
                sleep(0.5)
    except KeyboardInterrupt:
        print("\nCtrl-C pressed.  Cleaning up and exiting...")
    finally:
        wm.disconnect()


password_lookup()
print("end of run")
sys.exit()
