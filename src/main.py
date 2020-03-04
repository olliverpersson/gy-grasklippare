from components.gpios import SV, SH, init
from components.turn import turn
import time

init()

#SV.when_held = turn
#SH.when_held = turn

#while 1 == 1:
#	if SV.is_pressed:
#		turn(direction='right')
#	elif SH.is_pressed:
#		turn(direction='left')

while 1==1:
	if SH.is_pressed is False:
		turn('left')
	elif SV.is_pressed is False:
		turn('right')
	time.sleep(1)
