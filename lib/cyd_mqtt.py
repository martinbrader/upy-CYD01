from machine import unique_id
from ubinascii import hexlify
from umqttsimple import MQTTClient


class CYD_MQTT:

    def __init__(self, server, port, callback):
        self._server = server
        self._port = port
        self._callback = callback

    def connect_to_mqtt_server(self):
        # To create an MQTT client, we need to get the ESP unique ID.
        _client_id = hexlify(unique_id())
        self._client = MQTTClient(_client_id, self._server, self._port)
        self._client.set_callback(self._callback)
        self._client.connect()

    def subscribe(self, topic_sub):
        self._client.subscribe(topic_sub.encode(""))

    def publish(self, topic_pub, msg):
        self._client.publish(topic_pub.encode(), msg.encode())

    def check_for_messages(self):
        self._client.check_msg()
