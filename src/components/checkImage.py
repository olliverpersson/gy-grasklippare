from PIL import Image
import math
import pygame
import pygame.camera
import time
import json

data = []

with open('data.json') as json_file:

	data = json.load(json_file)

def checkImage():

	imgsrc = "__cache__.jpg"

	pygame.camera.init()

	cam = pygame.camera.Camera("/dev/video0",(640,480))
	cam.start()

	img = cam.get_image()

	pygame.image.save(img, imgsrc)

	# Ladda bild och ta ut rgb värde
	img = Image.open( imgsrc )
	img = img.resize( ( 1,1 ) )
	px = img.load()[0,0]

	r = int(px[0])
	g = int(px[1])
	b = int(px[2])

	distance = 500 #Så första alltid blir närmast i början
	index = 0

	print(time.time() - startAt)

	for i, item in enumerate(data):

   		# Pythagoras sats för avstånd till träningsdata
		d = math.sqrt( ( r - int(item["r"] ) )**2 + ( g - int(item["g"]) )**2 + ( b - int(item["b"] ) ) **2 )

    	if d < distance:

        	distance = d
        	index = i

	return data[index]["t"]
