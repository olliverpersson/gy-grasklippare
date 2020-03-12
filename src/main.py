from components.gpios import SV, SH, init
from components.turn import turn
from components.checkImage import checkImage
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

	while button.is_pressed:

#		if SH.is_pressed is False:
#			turn('left')
#		elif SV.is_pressed is False:
#			turn('right')
		time.sleep(1)
#		print("SV: " + str( SV.is_pressed ))
#		print("SH: " + str( SH.is_pressed ))
#		print( checkImage() )


#		print('Distance: ', SV.distance * 100)

		if SV.distance * 100 < 10:
			turn('left')
			print("Sensor detected object, turning left")

		if checkImage == 't' :
			turn('left')
			print("Camera detected object, turning left")
