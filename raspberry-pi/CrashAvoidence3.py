#type:ignore 
import board
import time
import digitalio
import busio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio
import adafruit_mpu6050


displayio.release_displays() #put this line just below your imports
i2c = busio.I2C(board.GP15, board.GP14)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP18)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)
mpu.gyro
mpu.acceleration
led1 = digitalio.DigitalInOut(board.GP0)
led1.direction = digitalio.Direction.OUTPUT


# # create the display group
splash = displayio.Group()

# # add title block to display group
title = "ANGULAR VELOCITY"
#the order of this command is (font, text, text color, and location)
text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)    

 # you will write more code here that prints the x, y, and z angular velocity values to the screen below the title. Use f strings!
 # Don't forget to round the angular velocity values to three decimal places

 # send display group to screen
display.show(splash)


while True:
    mpu.gyro
    text_area.text = (f"ANGULAR VELOCITY :)\nx : {mpu.gyro[0]} \ny : {mpu.gyro[1]} \nz : {mpu.gyro[2]}") #prints the velocities on the display, \n makes a line break
    
    led1.value = False #makes LED set to off

    if mpu.acceleration[0] > 9 or mpu.acceleration[0] < -9: #command when board is turned 90 degrees
        led1.value = True #turns LED on if it is tilted 90 degrees
 

