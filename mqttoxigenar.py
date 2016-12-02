#DOCS: https://pypi.python.org/pypi/paho-mqtt#installation
import paho.mqtt.client as mqtt
import threading

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    sendmesssage()
    

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


def sendmesssage():
    client.publish("iot-2/evt/oxigenar/fmt/json","{name:'python'}")
    threading.Timer(10,sendmesssage).start()


client = mqtt.Client(client_id="d:e4xlu6:arduino:nodemcu")
client.username_pw_set("use-token-auth", password="(tX0_77qL09-tqDrLl")
client.on_connect = on_connect
client.on_message = on_message

client.connect("e4xlu6.messaging.internetofthings.ibmcloud.com", 1883, 60)

client.loop_forever()
