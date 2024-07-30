# mpy6050aux.py

# The MPU9250 and HMC5883L are in parallel on the I2C bus. This code enabled the MPU9250's aux bypass mode so we can access the HMC5883L

from machine import I2C, Pin

# Define the I2C bus
i2c = I2C(0, scl=Pin(18), sda=Pin(19))  # Adjust the pins as necessary

# MPU-6050 I2C address
MPU6050_ADDRESS = 0x68 # 104

# Register addresses
MPU6050_RA_INT_PIN_CFG = 0x37 # 55
MPU6050_INTCFG_I2C_BYPASS_EN_BIT = 1

def set_i2c_bypass_enabled(enabled):
    # Read the current value of the INT_PIN_CFG register
    int_pin_cfg = i2c.readfrom_mem(MPU6050_ADDRESS, MPU6050_RA_INT_PIN_CFG, 1)[0]
    
    # Set or clear the I2C_BYPASS_EN bit
    if enabled:
        int_pin_cfg |= (1 << MPU6050_INTCFG_I2C_BYPASS_EN_BIT)
    else:
        int_pin_cfg &= ~(1 << MPU6050_INTCFG_I2C_BYPASS_EN_BIT)
    
    # Write back the updated value to the INT_PIN_CFG register
    i2c.writeto_mem(MPU6050_ADDRESS, MPU6050_RA_INT_PIN_CFG, bytes([int_pin_cfg]))

# Enable I2C bypass
set_i2c_bypass_enabled(True)


