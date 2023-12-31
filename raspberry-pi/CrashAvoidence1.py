#type: ignore

import board
import digitalio
import time
import adafruit_mpu6050
import busio


sda_pin = board.GP14
scl_pin = board.GP15
i2c = busio.I2C(board.GP15, board.GP14)
mpu = adafruit_mpu6050.MPU6050(i2c)
mpu.acceleration

while True: #loops command
    
    print(f"x angular acceleration: {mpu.acceleration[0]}") #print x value
    print(f"y angular acceleration: {mpu.acceleration[1]}") #print y value
    print(f"z angular acceleration: {mpu.acceleration[2]}") #print z value
    print("") #prints a gap
    time.sleep(0.5) #pauses for half a second before printing again
    
