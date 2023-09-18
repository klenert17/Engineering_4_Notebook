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

while True:
    
    print(f"x angular velocity: {mpu.gyro[0]}")
    print(f"y angular velocity: {mpu.gyro[1]}")
    print(f"z angular velocity: {mpu.gyro[2]}")
    print("")
    time.sleep(1)
    
