from gpiozero import DistanceSensor, Button
import time

print('Sensor test för Gräsklippare')

sensor1 = Button(pin=17)
sensor2 = Button(pin=18)

while True:
    if sensor1.is_pressed and sensor2.is_pressed:
        print('c')
    else:
        print('t')
    time.sleep(0.5)
