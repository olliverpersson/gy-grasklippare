from components.gpios import MVOO, MVPLUS, MVMINUS, MHOO, MHPLUS, MHMINUS, MKOO
from components.goForward import goForward
import time

def turn(direction):
  
  print("reversing...")
  
#to reversing

  MVOO.on()
  MHOO.on()
  MKOO.on()
  
  time.sleep(0.5)

  MVPLUS.on()
  MVMINUS.on()
  MHPLUS.on()
  MHMINUS.on()
  
  time.sleep(0.5)

#reversing

  MHOO.off()
  MVOO.off()
  
  time.sleep(2)
  
  MHOO.on()
  MVOO.on()
  
  time.sleep(0.5)

#to turning

  if direction == 'left':
    
    print("turning left")
    MVPLUS.off()
    MVMINUS.off()
    MHPLUS.on()
    MHMINUS.on()
  
  else:
    
    print("turning right")
    MVPLUS.on()
    MVMINUS.on()
    MHPLUS.off()
    MHMINUS.off()
   
  time.sleep(0.5)

#turning

  MHOO.off()
  MVOO.off()
    
  time.sleep(1)
  
  MKOO.off()

#to forward  

  goForward()

