import sys
import random
import time
from Adafruit_IO import MQTTClient
import serial . tools . list_ports
AIO_FEED_ID = ["bbc-led", "bbc-water","bbc-temp"] 
AIO_USERNAME = "Jackson25092002"
AIO_KEY = "aio_tPzT592ZDyA0RKYJo4bPhxCUq0oZ"

def connected(client):
    print("Ket noi thanh cong ...")
    for feed_id in AIO_FEED_ID:
        client.subscribe(feed_id)
        
def subscribe(client , userdata , mid , granted_qos):
    print("Subcribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " feed_id: " + feed_id)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    temp = random.randint(0, 100)
    print("Gui du lieu: ", temp)
    client.publish("bbc-temp", temp)
    time.sleep(5)