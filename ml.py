from PIL import Image
import math

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
    
# Ta in filsökväg
print("Filväg: ")
imgsrc = input()

# Ladda bild och ta ut rgb värde
img = Image.open( imgsrc )
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
    
print("Bilden ger: ")
print( data[index]["t"] )
