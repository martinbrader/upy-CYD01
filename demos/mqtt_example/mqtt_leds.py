from gc import collect as garbage_collect
from sys import exit as sys_exit
from time import sleep

from cyd_colours import BLUE, DARK_GREY, GREEN, RED, WHITE
from cyd_mqtt import CYD_MQTT
from cyd_utils import get_cyd_utils
from cyd_wifi_manager import WifiManager
from machine import reset as mc_reset

# ---------------MQTT set up-------------------------------
# EXAMPLE IP ADDRESS
# MQTT_SERVER = '192.168.1.144'
MQTT_SERVER = "broker.hivemq.com"
MQTT_PORT = 1883
TOPIC_COMMAND = "cyd_topic/cmd"
TOPIC_STATUS = "cyd_topic/status"


class MQTT_CMD:
    STATUS = "0"
    OFF = "1"
    RED = "2"
    GREEN = "3"
    BLUE = "4"

    @staticmethod
    def check(cmd):
        # check if valid command
        return len(cmd) == 1 and cmd in "01234"


# -----------Setup Led management---------------
class Led:
    def __init__(self, led_id, led, name, colour):
        self.id = led_id
        self.turn_on = led
        self.name = name
        self.colour = colour


def get_led_dict():
    # prepare dictionary of all led info
    _dict = {}
    _led = Led(MQTT_CMD.OFF, cyd_utils.led_off, "Off", DARK_GREY)
    _dict[_led.id] = _led
    _led = Led(MQTT_CMD.RED, cyd_utils.red_led_on, "Red", RED)
    _dict[_led.id] = _led
    _led = Led(MQTT_CMD.GREEN, cyd_utils.green_led_on, "Green", GREEN)
    _dict[_led.id] = _led
    _led = Led(MQTT_CMD.BLUE, cyd_utils.blue_led_on, "Blue", BLUE)
    _dict[_led.id] = _led
    return _dict


# ----------set up Event queue----------------
class EventQueue:
    def __init__(self):
        self.queue = []

    def add_event(self, event):
        self.queue.append(event)

    def process_events(self):
        while self.queue:
            event = self.queue.pop(0)
            # Process the event
            if MQTT_CMD.check(event):
                if event == MQTT_CMD.STATUS:
                    publish_status()
                else:
                    # must be led command
                    change_led_state(event)
            else:
                print("unknown event", event)


event_queue = EventQueue()


# ---Process MQTT commands ------------
def publish_status():
    mqtt.publish(TOPIC_STATUS, led_state.id)


def change_led_state(led_id):
    if led_id not in cyd_leds:
        raise ValueError("Bad led_id")
    _led = cyd_leds[led_id]
    global led_state
    led_state = _led
    led_state.turn_on()
    cyd_display.fill_circle(160, 120, 70, led_state.colour)
    display_msg("led state changed to: " + _led.name)
    # let others know
    publish_status()


# ----- Tidy up ---------------
def clean_up_and_finish(keyboard_interupt=False):
    # Disconnect from wifi and end the program
    if wm.is_connected():
        wm.disconnect()
    if keyboard_interupt:
        print("\nCtrl-C pressed. Cleaning up and exiting...")
    print("End of run")
    sys_exit()


# ------Display message to CYD and to console---------
def display_msg(msg):
    print(msg)
    # ensure message is exactly 40 chars long
    msg = "{:<40}".format(msg)[:40]
    cyd_display.draw_text8x8(0, 0, msg, WHITE)


# --------- wifi ----------------
def connect_to_wifi():
    try:
        display_msg("Looking for a wifi connection...")
        print("Press Ctrl-C to exit...")
        wm.connect()

        # Wait until connected to wifi
        while not wm.is_connected():
            sleep(0.5)
        sleep(3)
    except KeyboardInterrupt:
        clean_up_and_finish(True)


def handle_cmd(cmd):
    if MQTT_CMD.check(cmd):
        event_queue.add_event(cmd)
    else:
        print("unknown command", cmd)


# -----------MQTT routines------------------
# The callback function should accept as parameters the topic and the message.
def mqtt_callback(topic_in, msg_in):
    topic = topic_in.decode()
    msg = msg_in.decode()
    if topic == TOPIC_COMMAND:
        handle_cmd(msg)
    else:
        print("received unknown topic", topic)
    garbage_collect()  # after each message received


def mqtt_connect():
    while True:
        try:
            mqtt.connect_to_mqtt_server()
            display_msg("Connected to: " + MQTT_SERVER)
            print("Press Ctrl-C to exit...")
            break
        except OSError as e:
            reset_mqtt_connection()
        except KeyboardInterrupt:
            clean_up_and_finish(True)


# This function will be called in case the ESP32 or ESP8266 fails to connect to the broker.
# This function prints a message to inform that the connection was not successful.
# We wait 10 seconds. Then, we reset the ESP using the reset() method.
def reset_mqtt_connection():
    print("Failed to connect to MQTT broker. Reconnecting...")
    sleep(10)
    mc_reset()


# --------------start running ------------------
# activate the garbage collector.
garbage_collect()

# Get a reference to cyd_utils
cyd_utils = get_cyd_utils(width=320, height=240, rotation=90)
# get ref to cyd display screen
cyd_display = cyd_utils.cyd_display()
cyd_leds = get_led_dict()
# create initial led_status
led_state = cyd_leds[MQTT_CMD.OFF]

wm = WifiManager()
connect_to_wifi()

# ---- wifi connected, start mqtt-----------
display_msg("wifi connection established")

mqtt = CYD_MQTT(MQTT_SERVER, MQTT_PORT, mqtt_callback)

mqtt_connect()

change_led_state(led_state.id)  # intial display
mqtt.subscribe(TOPIC_COMMAND)

while True:
    try:
        mqtt.check_for_messages()
        event_queue.process_events()
    except OSError as e:
        reset_mqtt_connection()
        # try again
        mqtt_connect()
    except KeyboardInterrupt:
        clean_up_and_finish(True)
