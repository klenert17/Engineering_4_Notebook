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
led1 = digitalio.DigitalInOut(board.GP1)
led1.direction = digitalio.Direction.OUTPUT

with open("/data.csv", "a") as datalog:
    while True: #loops command

        time.sleep(0.5) #pauses for half a second before printing again
        datalog.write(f"{time.monotonic()},{mpu.acceleration[0]},{mpu.acceleration[1]},{mpu.acceleration[2]},{led1.value},\n") #prints time, x, y, z, and if the LED is on
        datalog.flush()

        led1.value = False #makes LED set to off

        if mpu.acceleration[0] > 9 or mpu.acceleration[0] < -9: #command when board is turned 90 degrees
            print("light")
            led1.value = True #turns LED on if it is tilted 90 degrees

