from components.checkImage import checkImage
from components.gpios import SV, SH
from components.turn import turn

SV.when_held = turn
SH.when_held = turn
