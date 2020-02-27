from components.gpios import MVOO, MVPLUS, MVMINUS, MHOO, MHPLUS, MHMINUS, MKOO

def goForward():
  
  MVOO.off()
  MHOO.off()

  MVPLUS.off()
  MVMINUS.off()
  MHPLUS.off()
  MHMINUS.off()

  MVOO.on()
  MHOO.on()
