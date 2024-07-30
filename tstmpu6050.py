# tstmpu6050.py

from machine import Pin, I2C
import mpu6050

i2c = I2C(0, scl=Pin(18), sda=Pin(19))

accelerometer = mpu6050.accel(i2c)
print(accelerometer.get_values())

import sys
del sys.modules['mpu6050']
del sys.modules['tstmpu6050'] # so we can run again with another import
