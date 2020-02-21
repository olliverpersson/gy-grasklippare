from gpiozero import LED
from time import sleep

rel2 = LED(26) #rel 2
rel1 = LED(19) #rel 1

rel2.off()

while True:
    print("on")
    rel1.on()
    sleep(3)
    print("off")
    rel1.off()
    sleep(3)