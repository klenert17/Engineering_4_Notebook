#type: ignore

import board
import digitalio
import time

for x in range(10, 0, -1): #makes moniter count down from 10 by -1
 time.sleep(1) #1 seconds bweteen each print
 print(x)

time.sleep(1)
print("LAUNCH") #States launch
