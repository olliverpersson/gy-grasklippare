from components.gpios import MVOO, MVPLUS, MVMINUS, MHOO, MHPLUS, MHMINUS, MKOO
import time

# stop the wheels, set a new state, turn them back on

def goForward():
  
  print("going forward")
  
  MVOO.on()
  MHOO.on()

  time.sleep(0.5)

  MVPLUS.off()
  MVMINUS.off()
  MHPLUS.off()
  MHMINUS.off()

  time.sleep(0.5)

  MVOO.off()
  MHOO.off()
