import os
import paho.mqtt.client as mqtt
import time


def read_file():
    readpath = 'readme.txt' 
    if not os.path.exists(readpath):
        print('Файл не найден!')
    else:
        with open(readpath, encoding='utf-8') as file:
            return [line for line in file.read().splitlines()]


if __name__ == '__main__':
    contents = read_file()
    mqttBroker = 'mqtt.eclipseprojects.io'
    client = mqtt.Client('Text_inside_file')
    client.connect(mqttBroker)

    for line in contents:
        client.publish('TESTINSIDEFILE', line)
        print(f'Опубликована строка: {line} в топик TEXTFILE')
        time.sleep(1)
