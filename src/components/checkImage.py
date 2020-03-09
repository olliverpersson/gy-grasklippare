from PIL import Image
import math
import pygame
import pygame.camera
import time
import json

data = []

with open('./resources/data.json') as json_file:

	data = json.load(json_file)

def checkImage():

	# TODO: Test this, not using __cache__.jpg might not work

	pygame.camera.init()

	#Tar bild
	cam = pygame.camera.Camera("/dev/video0",(640,480))
	cam.start()
	pil_string_image = pygame.image.tostring(cam.get_image(),"RGBA",False)
	img = Image.frombytes("RGBA",(1280,720),pil_string_image)

	#Tar ut rgb värde
	img = img.resize( ( 1,1 ) )
	px = img.load()[0,0]

	r = int(px[0])
	g = int(px[1])
	b = int(px[2])

	distance = 500 #Så första alltid blir närmast i början
	index = 0

	for i, item in enumerate(data):

   		# Pythagoras sats för avstånd till träningsdata
		d = math.sqrt( ( r - int(item["r"] ) )**2 + ( g - int(item["g"]) )**2 + ( b - int(item["b"] ) ) **2 )

    	if d < distance:

        	distance = d
        	index = i

	return data[index]["t"]
