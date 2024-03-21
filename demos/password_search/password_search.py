"""Search online for pwned passwords."""

import gc
from hashlib import sha1
from utime import sleep


from touch_keyboard import TouchKeyboard
from ubinascii import hexlify
from urequests2 import get
from xglcd_font import XglcdFont
from xpt2046 import Touch
from MJB_wifi_manager import WifiManager

class PwnLookup(object):
    """Checks if password is pwned."""

    def __init__(self, wlan, spi2, dc=2, cs1=15, rst=15, cs2=33, rotation=270):
        self.wlan = wlan
        # Set up display
        self.display = Display(
            spi1,
            dc=Pin(dc),
            cs=Pin(cs1),
            rst=Pin(rst),
            width=320,
            height=240,
            rotation=rotation,
        )

        # Turn on display backlight
        backlight = Pin(21, Pin.OUT)
        backlight.on()

        self.display.clear()

        # Load font
        self.unispace = XglcdFont("fonts/Unispace12x24.c", 12, 24)

        # Set up Keyboard
        self.keyboard = TouchKeyboard(self.display, self.unispace)

        # Set up touchscreen
        self.xpt = Touch(
            spi2, cs=Pin(cs2), int_pin=Pin(36), int_handler=self.touchscreen_press
        )

        # set up network
        # self._do_connect()
        ssid1 = "ssid1"
        password1 = "password1"
        ssid2 = "ssid2"
        password2 = "password2"

        self._connect_to_wifi(ssid1, password1, ssid2, password2)

    def _do_connect(self):
        self.wlan = WLAN(STA_IF)
        self.wlan.active(True)
        self.wlan.scan()
        if not self.wlan.isconnected():
            print("connecting to network...")
            self.wlan.connect("ssid2", "password2")
            # self.wlan.connect("ssid1", "password1")
            while not self.wlan.isconnected():
                pass
        print("network config:", self.wlan.ifconfig())

    # --------------------------------
    def _connect_to_wifi(self, ssid1, password1, ssid2, password2):
        self.wlan = WLAN(STA_IF)
        self.wlan.active(True)

        while not self.wlan.isconnected():
            print("Connecting to network...")
            self.wlan.connect(ssid1, password1)
            for _ in range(10):
                if self.wlan.isconnected():
                    break
                sleep(1)
            else:
                print("Failed to connect to " + ssid1 + ", trying " + ssid2 + "...")
                self.wlan.active(False)
                sleep(0.5)
                self.wlan.active(True)
                self.wlan.connect(ssid2, password2)
                for _ in range(10):
                    if self.wlan.isconnected():
                        break
                    sleep(1)
                else:
                    print(
                        "Failed to connect to " + ssid2 + " Retrying in 10 seconds..."
                    )
                    sleep(10)

        print("Network config:", self.wlan.ifconfig())

        # --------------------------------

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

            self.keyboard.show_message("Searching...", color565(0, 0, 255))
            try:
                hits = self.lookup(pwd)

                if hits:
                    # Password found
                    msg = "PASSWORD HITS: {0}".format(hits)
                    self.keyboard.show_message(msg, color565(255, 0, 0))
                else:
                    # Password not found
                    msg = "PASSWORD NOT FOUND"
                    self.keyboard.show_message(msg, color565(0, 255, 0))
            except Exception as e:
                if hasattr(e, "message"):
                    self.keyboard.show_message(e.message[:22], color565(255, 255, 255))
                else:
                    self.keyboard.show_message(str(e)[:22], color565(255, 255, 255))

            self.keyboard.waiting = True
            self.keyboard.locked = False


def password_lookup():
wm = WifiManager()
wm.connect()

    PwnLookup(spi1, spi2)

    while True:
        sleep(0.1)


password_lookup()

# print("press Ctrl-C to exit...")
# try:
#     while True:
#         if wm.is_connected():
#             print("Connected!")
#         else:
#             print("Disconnected!")
#         sleep(10)
# except KeyboardInterrupt:
#     print("\nCtrl-C pressed.  Cleaning up and exiting...")
# finally:
#     wm.disconnect()
print("end of run")
