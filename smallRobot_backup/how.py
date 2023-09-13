from __future__ import division
import RPi.GPIO as GPIO
import time
import Adafruit_PCA9685
import math
import busio
from board import SCL, SDA
from adafruit_servokit import ServoKit



# 초음파 센서에 연결된 핀 번호 설정
TRIG_PIN = 21
ECHO_PIN = 20

# PCA9685 모듈 초기화
kit = ServoKit(channels=16)

i2c = busio.I2C(SCL, SDA)
pwm = Adafruit_PCA9685.PCA9685()

# 서보모터와 DC 모터에 연결된 PCA9685 모듈의 채널 번호 설정
servo_channels = [1, 2, 3, 4, 5, 6]  # 6개의 서보모터 채널
dc_channels = [7, 8, 9, 10]  # 4개의 DC 모터 채널

# 서보모터의 최소 및 최대 펄스 길이
servo_min_pulse = 750  # 예시 값, 실제 서보모터에 맞게 조정해야 함
servo_max_pulse = 2250  # 예시 값, 실제 서보모터에 맞게 조정해야 함

# DC 모터의 최소 및 최대 속도
dc_min_speed = -1  # 최소 속도
dc_max_speed = 1  # 최대 속도

# 초음파 센서 핀 설정
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)


def set_servo_angle(channel, angle):
    pwm_value = int((angle / 180.0) * (servo_max_pulse - servo_min_pulse) + servo_min_pulse)
    kit.servo[channel].set_pulse_width_range(servo_min_pulse, servo_max_pulse)
    kit.servo[channel].angle = pwm_value




