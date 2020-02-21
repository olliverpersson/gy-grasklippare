#import pygame
#import pygame.camera
#from colorthief import ColorThief

from PIL import Image

#pygame.camera.init()
#camlist = pygame.camera.list_cameras() #Camera detected or not
#
#print( camlist )

data =  [{"file":"img0.jpeg", "type": "cut"},
        {"file":"img1.jpeg", "type": "cut"},
        {"file":"img2.jpeg", "type": "cut"},
        {"file":"img3.jpeg", "type": "cut"},
        {"file":"img4.jpeg", "type": "cut"},
        {"file":"img5.jpeg", "type": "cut"},
        {"file":"img6.jpeg", "type": "cut"},
        {"file":"img7.jpeg", "type": "cut"},
        {"file":"img8.jpeg", "type": "cut"},
        {"file":"img9.jpeg", "type": "cut"},
        {"file":"img10.jpeg", "type": "cut"},
        {"file":"img11.jpeg", "type": "cut"},
        {"file":"img12.jpeg", "type": "turn"},
        {"file":"img13.jpeg", "type": "turn"},
        {"file":"img14.jpeg", "type": "turn"},
        {"file":"img15.jpeg", "type": "turn"},
        {"file":"img16.jpeg", "type": "turn"},
        {"file":"img17.jpeg", "type": "turn"},
        {"file":"img18.jpeg", "type": "turn"},
        {"file":"img19.jpeg", "type": "turn"},
        {"file":"img20.jpeg", "type": "turn"},
        {"file":"img21.jpeg", "type": "night"},
        {"file":"img22.jpeg", "type": "turn"},
        {"file":"img23.jpeg", "type": "turn"},
        {"file":"img24.jpeg", "type": "turn"},
        {"file":"img25.jpeg", "type": "turn"},
        {"file":"img26.jpeg", "type": "turn"},
        {"file":"img27.jpeg", "type": "turn"},
        {"file":"img28.jpeg", "type": "turn"},
        {"file":"img29.jpeg", "type": "night"},
        {"file":"img30.jpeg", "type": "night"},
        {"file":"img31.jpeg", "type": "night"}]

correct = 0

i = 0

for item in data:
    
    img = Image.open("images/" + item["file"] )
    img = img.resize( ( 1,1 ) )
    px = img.load()[0,0]
    
    r = px[0]
    g = px[1]
    b = px[2]

    if r < 60 and g < 60 and b < 60 and item["type"] == "night":
        
        correct  += 1
    
    elif r > 50 and g > 100 and b > 5 and item["type"] == "cut":
        
        correct += 1
    
    elif item["type"] == "turn":
        
        correct += 1
        
    else:
        print( item["file"] + " is incorrect, should be " + item["type"])
        print( "rgb: (%s,%s,%s)" % (r,g,b) )
    
    i += 1
    

print( "Correct: " + str( correct/len(data) ))

#cam = pygame.camera.Camera("/dev/video0",(640,480))
#cam.start()
#img = cam.get_image()
#pygame.image.save(img,"filename.jpg")