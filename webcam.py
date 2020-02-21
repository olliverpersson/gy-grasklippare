from PIL import Image
import math
import pygame
import pygame.camera
import time

imgsrc = "__cache__.jpg"

print(time.time())

pygame.camera.init()

cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()

img = cam.get_image()

print(time.time())

pygame.image.save(img, imgsrc)

bild = Image.open( imgsrc )

bild.show(command='fim')
