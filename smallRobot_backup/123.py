from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685
from adafruit_servokit import ServoKit

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()
kit = ServoKit(channels=16)
# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 750  # Min pulse length out of 4096
servo_max = 2250  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

def set_servo_angle(channel, angle):
    pwm_value = int((angle / 180.0) * (servo_max - servo_min) + servo_min)
    kit.servo[channel].set_pulse_width_range(servo_min, servo_max)
    kit.servo[channel].angle = pwm_value
# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

 # Move servo on channel O between extremes.
# pwm.set_pwm(4, 0, 750)
# time.sleep(1)
# pwm.set_pwm(4, 0, 0)
# time.sleep(1)
# pwm.set_pwm(4, 0, 1000)
# time.sleep(1)
pwm.set_pwm(4, 0, 2100)
time.sleep(0.3)
# 
pwm.set_pwm(4, 0, 0)
time.sleep(0.5)

pwm.set_pwm(4, 0, 2250)
time.sleep(0.5)


pwm.set_pwm(4, 0, 0)
time.sleep(0.5)


pwm.set_pwm(4, 0, -2250)
time.sleep(0.5)


pwm.set_pwm(4, 0, 0)
time.sleep(0.5)

pwm.set_pwm(4, 0, 2250)
time.sleep(0.5)


pwm.set_pwm(4, 0, 0)
time.sleep(0.5)





pwm.set_pwm(5, 0, 0)
time.sleep(0.5)

pwm.set_pwm(5, 0, 2250)
time.sleep(0.5)


pwm.set_pwm(5, 0, 0)
time.sleep(0.5)


pwm.set_pwm(5, 0, 2250)
time.sleep(0.5)


pwm.set_pwm(5, 0, 0)
time.sleep(0.5)

pwm.set_pwm(5, 0, 2250)
time.sleep(0.5)


pwm.set_pwm(5, 0, 0)
time.sleep(0.5)

# 
# pwm.set_pwm(4, 0, 2250)
# time.sleep(0.5)
# 
# pwm.set_pwm(4, 0, 0)
# time.sleep(1)
# 
# pwm.set_pwm(4, 0, 2250)
# time.sleep(0.5)
# 
# pwm.set_pwm(4, 0, 0)
# time.sleep(1)
# 
# 
# pwm.set_pwm(4, 0, 2250)
# time.sleep(0.5)
# 
# pwm.set_pwm(4, 0, 0)
# time.sleep(1)