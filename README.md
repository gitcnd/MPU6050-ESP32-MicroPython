# MPU6050-ESP32-MicroPython
Simple library for MPU6050 on ESP32 with micropython

The ESP32 has hardware i2c, so this lib has the software-only i2c methods removed

SCL connected to pin 5, SDA to pin 4
example usage:

```python
from machine import I2C, Pin
import mpu6050
i2c = I2C(0, scl=Pin(5), sda=Pin(4))
accelerometer = mpu6050.accel(i2c)
accelerometer.get_values()
{'GyZ': -132, 'GyY': 457, 'GyX': -416, 'Tmp': 22.31823, 'AcZ': 16948, 'AcY': -508, 'AcX': -1000}

```
Accelerometer/Gyroscope values are in int16 range (-32768 to 32767)
If the mpu6050 loses power, you have to call __init__() again
