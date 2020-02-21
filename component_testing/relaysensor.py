from gpiozero import LED, Button
from time import sleep

rel2 = LED(26) #rel 2
rel1 = LED(19) #rel 1

rel2.off()
rel1.off()

sensor1 = Button(pin=3)
sensor2 = Button(pin=17)
sensor1pwr = LED(2)
sensor2pwr = LED(4)

sensor1pwr.on()
sensor2pwr.on()

while True:
    print(sensor1.is_pressed)
    print(sensor2.is_pressed)
    print("----------")
    
    if sensor2.is_pressed:
        print('Klipper')
        rel2.on()
        rel1.on()
    else:
        rel2.off()
        rel2.off()
        print('Ett hinder framför')
    sleep(0.5)