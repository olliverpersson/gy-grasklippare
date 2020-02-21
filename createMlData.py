from PIL import Image

file = open('data.txt','a')

print( "Filväg: " )
src = input()

print( "Visar bilden klipp, natt eller vänd? (c/n/t)" )
txt = input()

while txt != "c" and txt != "n" and txt != "t":
    
    print("type 'c' or 'n' or 't'")
    txt = input()

img = Image.open( src )
img = img.resize( ( 1,1 ) )
px = img.load()[0,0]

print( "rgb: " + str(px) )

file.write( "\n" + str(px[0]) + " " + str(px[1]) + " " + str(px[2]) + " " + txt)
file.close()

print("Bilden har lagts till i träningsdatan.")