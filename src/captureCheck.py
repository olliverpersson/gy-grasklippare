from PIL import Image
import math
import pygame
import pygame.camera
import time

imgsrc = "__cache__.jpg"

startAt = time.time()
print(startAt)

pygame.camera.init()

cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()

img = cam.get_image()

print(time.time() - startAt)

pygame.image.save(img, imgsrc)

print(time.time() - startAt)

file = open('data.txt', 'r')

data = []

for line in file:

    txt = line.split(' ')

    data.append({
        "r" : txt[0],
        "g" : txt[1],
        "b" : txt[2],
        "t" : txt[3][0]
    })

print(time.time() - startAt)

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

print("Bilden ger: ")
print( data[index]["t"] )
print("Total time: " + (time.time() - startAt))
