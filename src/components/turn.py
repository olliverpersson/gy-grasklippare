from components.gpios import MVOO, MVPLUS, MVMINUS, MHOO, MHPLUS, MHMINUS, MKOO
from components.goForward import goForward
import time

def turn(direction):
  
  MVOO.off()
  MHOO.off()
  MKOO.off()
  
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
