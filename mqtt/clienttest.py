# coding: UTF-8
import paho.mqtt.client as paho
import time
import random


def on_connect(client, userdata, flags, rc):
    msg=['Connection successful',
         'Connection refused - incorrect protocol version'
         'Connection refused - invalid client identifier',
         'Connection refused - server unavailable',
         'Connection refused - bad username or password',
         'Connection refused - not authorised'
         ]
    print("连接MQTT服务器:",msg[rc])


def on_publish(client, userdata, mid):
    print("消息id: " + str(mid))


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_message(client, userdata, msg):
    data = msg.payload.decode("utf-8")
    print(msg.topic + " " + str(msg.qos) + "=" , float(data))


client = paho.Client()
client.on_connect=on_connect
client.on_publish = on_publish
client.on_message = on_message
client.connect("broker.mqttdashboard.com", 1883)
client.subscribe("/temperature", qos=1)
client.loop_start()

while True:
    temperature = random.uniform(10,50)
    (rc, mid) = client.publish("/temperature", str(temperature), qos=1)
    time.sleep(3)
