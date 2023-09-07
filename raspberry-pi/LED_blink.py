#type: ignore

import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True   #led turns on
    time.sleep(0.5)    #for 0.5 seconds
    led.value = False  #led turns off
    time.sleep(0.5)    #for 0.5 seconds