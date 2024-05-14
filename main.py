import sys
import serial . tools . list_ports
import random
import time
from Adafruit_IO import MQTTClient
AIO_FEED_ID = ["bbc-led", "bbc-water","bbc-temp"] 
AIO_USERNAME = "Jackson25092002"
AIO_KEY = "aio_AyUA88eWNwLqDawMgNuYsVbxTr7S"

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


def getPort():
    ports = serial.tools.list_ports.comports()
    N = len(ports)
    commPort = "None"
    for i in range(0, N):
        port = ports[i]
        strPort = str(port)
        if "COM6" in strPort:
            splitPort = strPort.split(" ")
            commPort = splitPort[0]
    return commPort

isMicrobitConnected = False
if getPort() != "None":
    ser = serial.Serial(port=getPort(), baudrate=115200)
    isMicrobitConnected = True

mess = ""

def processData(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    if splitData[1] == "TEMP":
        client.publish("bbc-temp", splitData[2])
    if splitData[1] == "LED":
        client.publish("bbc-led", splitData[2])
        
mess = ""
     
def readSerial():
    bytesToRead = ser.inWaiting()
    if bytesToRead > 0:
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(mess[start : end + 1])
            if end == len(mess):
                mess = ""
            else:
                mess = mess[end + 1 :]
   
while True:
    if isMicrobitConnected:
        readSerial()
    # value = random.randint(0, 100)
    # print("Cap nhat:", value)
    # client.publish("bbc-temp", value)
    time.sleep(1)
    