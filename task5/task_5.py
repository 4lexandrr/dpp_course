import cv2 as cv
import numpy as np
import paho.mqtt.client as mqtt
import time


def show_clicked(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        x_y.append((x, y))
        print(x_y)


def publish_positions(content):
    """ функция публикации коорлинат в топик """ 
    position = content
    mqttBroker = 'mqtt.eclipseprojects.io'
    client = mqtt.Client('Ckicks_coords')
    client.connect(mqttBroker)

    client.publish('position', str(coord for coord in position))
    print(f'Опубликована строка: {position} в топик position')


if __name__ == '__main__':
    x_y = []
    capture = cv.VideoCapture(0)

    while True:
        ret, frame = capture.read()
        activation_key = cv.waitKey(1)

        for coord in x_y:
            cv.rectangle(frame, (coord[0]-5, coord[1]-5), (coord[0]+5, coord[1]+5), (0, 255, 0), 2)
        cv.imshow('frame', frame)
        cv.setMouseCallback('frame', show_clicked)

        if activation_key == ord('q'):
            break
        
        if activation_key == ord('c'):
            publish_positions(x_y)
            x_y = []

    capture.release()
    cv.destroyAllWindows()