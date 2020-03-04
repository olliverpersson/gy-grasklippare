from components.gpios import MVOO, MVPLUS, MVMINUS, MHOO, MHPLUS, MHMINUS, MKOO
import time

# stop the wheels, set a new state, turn them back on

def goForward():
  
  print("going forward")
  
  MVOO.on()
  MHOO.on()

  time.sleep(0.5)

  MVPLUS.on()
  MVMINUS.on()
  MHPLUS.on()
  MHMINUS.on()

  time.sleep(0.5)

  MVOO.off()
  MHOO.off()
