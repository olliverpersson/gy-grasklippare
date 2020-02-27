from components.gpios import MVOO, MVPLUS, MVMINUS, MHOO, MHPLUS, MHMINUS, MKOO
from components.goForward import goForward
import time

def turn(direction):
  
  print("reversing...")
  
  MVOO.off()
  MHOO.off()
  MKOO.off()
  
  MVPLUS.on()
  MVMINUS.on()
  MHPLUS.on()
  MHMINUS.on()
  
  MHOO.on()
  MVOO.on()
  
  time.sleep(2)
  
  MHOO.off()
  MVOO.off()
  
  time.sleep(0.5)
  
  if direction == 'left':
    
    print("turning left")
    MVPLUS.on()
    MVMINUS.on()
    MHPLUS.off()
    MHMINUS.off()
  
  else:
    
    print("turning right")
    MVPLUS.off()
    MVMINUS.off()
    MHPLUS.on()
    MHMINUS.on()
   
  time.sleep(0.5)
    
  MHOO.on()
  MVOO.on()
    
  time.sleep(2)
  
  MKOO.on()
  
  goForward()
