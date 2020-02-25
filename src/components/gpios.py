from gpiozero import LED, BUTTON

# Every GPIO connection is initiated here

MVOO = LED(16)
MVOO.on()

MVPLUS = LED(20)
MVPLUS.off()

MVMINUS = LED(21)
MVMINUS.off()

MHOO = LED(13)
MHOO.on()

MHPLUS = LED(19)
MHPLUS.off()

MHMINUS = LED(26)
MHMINUS.off()

MKOO = LED(6)
MKOO.on()

SV = BUTTON(4) #SVS

SH = BUTTON(23) #SHS
