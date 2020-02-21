from colorthief import ColorThief
from PIL import Image

filedir = input()

def getLoopColor(imgsrc):
    
    img = Image.open(imgsrc)
    px = img.load()
    size = img.size
    
    r = 0
    g = 0
    b = 0
    
    pxcount = 0
    
    for x in range(0, size[0]): 
        
        for y in range(0, size[1]): 
            
            c = px[x,y]
            
            r += c[0]
            g += c[1]
            g += c[2]
            
            pxcount += 1
    
    r = r/pxcount
    g = g/pxcount
    b = b/pxcount
    
    return (r,g,b)

def getScaleColor(imgsrc):

    img = Image.open(imgsrc)
    
    img = img.resize( ( 1,1 ) )
    
    return img.load()[0,0]

def getLanczosColor(imgsrc):

    img = Image.open(imgsrc)
    
    img = img.resize( ( 1,1 ), Image.LANCZOS )
    
    return img.load()[0,0]

def getHammingColor(imgsrc):

    img = Image.open(imgsrc)
    
    img = img.resize( ( 1,1 ), Image.HAMMING )
    
    return img.load()[0,0]
    
print( getLoopColor(filedir) )

print( getScaleColor(filedir) )

print( getLanczosColor(filedir) )

print( getHammingColor(filedir) )

color_thief = ColorThief( filedir )
dominant_color = color_thief.get_color(quality=2)
print( dominant_color )