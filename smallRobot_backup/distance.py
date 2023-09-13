
import time
import busio
import math
import RPi.GPIO as GPIO

from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import motor
from adafruit_servokit import ServoKit
from drive_class import drivingclass
kit = ServoKit(channels=16)

# 초음파 센서에 연결된 핀 번호 설정
TRIG_PIN = 21
ECHO_PIN = 20

# 초음파 센서 핀 설정
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)


car = drivingclass()

def set_servo_angle(channel,angle):
    kit.servo[channel].angle=angle

def get_distance():
    GPIO.output(TRIG_PIN,True)
    time.sleep(0.00001)        # 10uS의 펄스 발생을 위한 딜레이
    GPIO.output(TRIG_PIN, False)
        
    while GPIO.input(ECHO_PIN)==0:
        start = time.time()     # Echo핀 상승 시간값 저장
            
    while GPIO.input(ECHO_PIN)==1:
        stop = time.time()      # Echo핀 하강 시간값 저장
            
    check_time = stop - start
    distance = check_time * 34300 / 2
    print("Distance : %.1f cm" % distance)
    time.sleep(0.4)
    return distance

def calculate_angle(distance):
    #h=계단높이
    #r=자동차 바퀴 반지름
    distance=get_distance()
    angle_rad = math.atan(8 / (2 + int(distance)))
    angle=math.degrees(angle_rad)
    print("Angle : %.1f" % angle)
    return angle
    

#서보모터 구동
#앞대가리 
def fd_up():
    angle=calculate_angle(distance)
    set_servo_angle(2,angle) #서보(5) 올라갈준비
    set_servo_angle(3,angle) #서보(6) 올라갈준비
    time.sleep(1)

#중간
def md_up():
    angle=calculate_angle()/2 #angle의 반만 회전-무게때문에 
    set_servo_angle(servo_channels[2],angle) #서보(3) 올라갈준비
    set_servo_angle(servo_channels[3],angle) #서보(4) 올라갈준비
    time.sleep(1)
    
    
def fd():
    set_servo_angle(3, 10)
    set_servo_angle(4, 170)
    time.sleep(1)









def md():
    set_servo_angle(2, 90)
    set_servo_angle(3, 90)
    time.sleep(1)



car.goForward(1)
time.sleep(0.5)
car.stop()

set_servo_angle(7, 125)
set_servo_angle(11, 55)
time.sleep(1)



car.goForward(1)
time.sleep(0.5)
car.stop()

time.sleep(1)

set_servo_angle(7, 90)
set_servo_angle(11, 90)
time.sleep(1)

set_servo_angle(3,90)
set_servo_angle(4,90)
time.sleep(1)


set_servo_angle(3,160)
set_servo_angle(4,10)
time.sleep(1)


car.goForward(1)
time.sleep(2)

set_servo_angle(3,160)
set_servo_angle(4,10)
time.sleep(1)


set_servo_angle(14,90)
set_servo_angle(15,90)
time.sleep(1)

# 
# car.goForward(1)
# time.sleep(2)

# set_servo_angle(14,180)
# set_servo_angle(15,0)
# time.sleep(1)
# 
# 
# car.goForward(1)
# time.sleep(2)
#  
# 
# car.stop()
# 
# time.sleep(1)







# set_servo_angle(3,160)
# set_servo_angle(4,10)
# time.sleep(1)
# 
# 
# 
# set_servo_angle(7, 125)
# set_servo_angle(11, 55)
# time.sleep(1)
# 
# 
# set_servo_angle(7, 90)
# set_servo_angle(11, 90)
# time.sleep(1)
# 
# set_servo_angle(3,90)
# set_servo_angle(4,90)
# time.sleep(1)
#   
# 
# 
# set_servo_angle(3,160)
# set_servo_angle(4,10)
# time.sleep(1)
# 
# 
# set_servo_angle(14,150)
# set_servo_angle(15,30)
# time.sleep(1)
# 
# set_servo_angle(14,180)
# set_servo_angle(15,0)
# time.sleep(1)







def basic():
    
    set_servo_angle(10, 90)
    set_servo_angle(11, 90)
    time.sleep(1)
    set_servo_angle(3,160)
    set_servo_angle(4,10)
    time.sleep(1)
    
    
# calculate_angle(distance)
# while True:
#     
#     set_servo_angle(11, 90)
#     set_servo_angle(12, 90)
#     time.sleep(1)
#     set_servo_angle(3, 90)
#     set_servo_angle(4, 90)
#     time.sleep(1)
# 
#     set_servo_angle(11, 60)
#     set_servo_angle(12, 120)
#     time.sleep(1)
#     set_servo_angle(3, 60)
#     set_servo_angle(4, 120)
#     time.sleep(1)
# # 
# set_servo_angle(3, 60)
# set_servo_angle(4, 120)
# time.sleep(1)
# 
# 
# set_servo_angle(3, 30)
# set_servo_angle(4, 150)
# time.sleep(1)
# 
# set_servo_angle(3, 20)
# set_servo_angle(4, 10)
# time.sleep(1)
