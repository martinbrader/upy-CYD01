# Description: WiFi Manager for ESP32 using MicroPython.
# Based on code from https://github.com/ferreira-igor/micropython-wifi_manager/blob/main/wifi_manager.py

from network import STA_IF, WLAN
from utime import sleep, sleep_ms


class WifiManager:

    def __init__(self):
        self.wlan_sta = WLAN(STA_IF)
        self.wlan_sta.active(True)

        # The file were the credentials will be stored.
        # There is no encryption, it's just a plain text archive. Be aware of this security problem!
        self.wifi_credentials = "credentials.txt"

        # Prevents the device from automatically trying to connect to the last saved network without first going through the steps defined in the code.
        self.wlan_sta.disconnect()

    def connect(self):
        if self.wlan_sta.isconnected():
            return True
        profiles = self.read_credentials()
        for ssid, *_ in self.wlan_sta.scan():
            ssid = ssid.decode("utf-8")
            if ssid in profiles:
                password = profiles[ssid]
                if self.wifi_connect(ssid, password):
                    return True
        print("Could not connect to any WiFi network.")
        return False

    def disconnect(self):
        if self.wlan_sta.isconnected():
            self.wlan_sta.disconnect()

    def is_connected(self):
        return self.wlan_sta.isconnected()

    def get_address(self):
        return self.wlan_sta.ifconfig()

    def read_credentials(self):
        lines = []
        try:
            with open(self.wifi_credentials) as file:
                lines = file.readlines()
        except Exception as error:
            print("read_credentials error:", error)

        profiles = {}
        for line in lines:
            ssid, password = line.strip().split(",")
            profiles[ssid] = password
        return profiles

    def wifi_connect(self, ssid, password):
        print("Trying to connect to:", ssid)
        self.wlan_sta.connect(ssid, password)
        for _ in range(100):
            if self.wlan_sta.isconnected():
                print("\nConnected! Network information:", self.wlan_sta.ifconfig())
                return True
            else:
                print(".", end="")
                sleep_ms(200)
        print("\nConnection failed!")
        self.wlan_sta.disconnect()
        return False


# Example of usage

# wm = WifiManager()
# wm.connect()

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
# print("end of run")
