# imports
import board
import time
from digitalio import DigitalInOut, Direction
import random
from analogio import AnalogIn
import time
import pwmio

# configurations & setup of leds
blue = pwmio.PWMOut(board.D3, frequency=5000, duty_cycle=0)
pot = AnalogIn(board.A1)
norm_v = 32767 / 65535
rng = 0.5 - 0.05
minm = 0.05
maxm = 65535
delay = (pot.value / maxm * rng + minm)

        
#main (infinte loop)
while True:
    blue.duty_cycle = pot.value
