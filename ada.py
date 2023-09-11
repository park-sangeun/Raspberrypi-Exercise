from adafruit_servokit import ServoKit
from time import sleep
kit=ServoKit(channels=16)
servo_channel=4

def move_servo(angle):
    kit.servo[servo_channel].angle = angle
      # Adjust the sleep time to set the speed of movement

try:
    # Move the servo to 45 degrees
    move_servo(45)

    # Wait for a brief moment before moving to the next position
    sleep(1)

    # Move the servo to 90 degrees
    move_servo(90)

    # Wait for a brief moment before moving to the next position
    sleep(1)

    # Move the servo to 180 degrees
    move_servo(180)
except KeyboardInterrupt:
    # Handle keyboard interrupt (Ctrl+C)
    pass