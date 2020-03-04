from gpiozero import LED, Button
import time

# Every GPIO connection is initiated here

MVOO = LED(16)

MVPLUS = LED(20)

MVMINUS = LED(21)

MHOO = LED(13)

MHPLUS = LED(19)

MHMINUS = LED(26)

MKOO = LED(6)

SV = Button(4) #SVS

SH = Button(23) #SHS

def init():
	print("turning everything to it's initial state")

	MHOO.on()
	MVOO.on()

	time.sleep(0.5)

	MVPLUS.on()
	MVMINUS.on()

	MHPLUS.on()
	MHMINUS.on()

	time.sleep(0.5)

	MKOO.off()
	MVOO.off()
	MHOO.off()
