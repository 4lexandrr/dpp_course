import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(str(rc)))
    client.subscribe('TESTINSIDEFILE')


def on_message(client, userdata, message):
    print('Получено сообщение: ', str(message.payload.decode('utf-8')))


mqttBroker = 'mqtt.eclipseprojects.io'
client = mqtt.Client('SmartPhone')
client.connect(mqttBroker)

client.loop_start()
client.on_connect = on_connect
client.on_message = on_message
time.sleep(30)
client.loop_end()