import time
import busio
import math
import RPi.GPIO as GPIO

from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import motor
from adafruit_servokit import ServoKit

class drivingclass:

    def __init__(self):
        print("init.............")
        self.i2c = busio.I2C(SCL, SDA)

        self.pca = PCA9685(self.i2c, address=0x40)
        self.pca.frequency = 100

        self.pca.channels[0].duty_cycle = 0xFFFF
        self.pca.channels[6].duty_cycle = 0xFFFF
        #self.pca.channels[15].duty_cycle = 0xFFFF
        #self.pca.channels[10].duty_cycle = 0xFFFF

        self.motor1 = motor.DCMotor(self.pca.channels[7], self.pca.channels[8]) #
        self.motor2 = motor.DCMotor(self.pca.channels[1], self.pca.channels[2])
#         self.motor3 = motor.DCMotor(self.pca.channels[11], self.pca.channels[12])
#         self.motor4 = motor.DCMotor(self.pca.channels[13], self.pca.channels[14])
        print("init.............finish")

    def goForward(self, speed):
        print(self)
        self.motor1.throttle = speed
        self.motor2.throttle = speed
        
        time.sleep(1)

    def goBackward(self, speed):
        self.motor1.throttle = -speed
        self.motor2.throttle = -speed
       
        time.sleep(1)

    def goRight(self, speed):
        self.motor1.throttle = -speed
        self.motor2.throttle = speed
        time.sleep(1)

    def goLeft(self, speed):
        self.motor1.throttle = speed
        self.motor2.throttle = -speed
        time.sleep(1)

    def goright_diagonal(self, speed):
        self.motor1.throttle = 0
        self.motor2.throttle = speed
        time.sleep(1)

    def goleft_diagonal(self, speed):
        self.motor1.throttle = speed
        self.motor2.throttle = 0
        time.sleep(1)

    def backright_diagonal(self, speed):
        self.motor1.throttle = -speed
        self.motor2.throttle = 0
        time.sleep(1)

    def backleft_diagonal(self, speed):
        self.motor1.throttle = 0
        self.motor2.throttle = -speed
        time.sleep(1)

    def turnRight(self, speed):
        self.motor1.throttle = speed
        self.motor2.throttle = -speed
        time.sleep(1)

    def turnLeft(self, speed):
        self.motor1.throttle = -speed
        self.motor2.throttle = speed
        time.sleep(1)

    def stop(self):
        self.motor1.throttle = 0
        self.motor2.throttle = 0
        time.sleep(1)
        
def set_servo_angle(channel,angle):
    kit.servo[channel].angle=angle
    

# def sweep_servo():
#     set_servo_angle(,) # 서보모터를 0도로 초기화
#     time.sleep(1)        

#거리 측정 함수
def get_distance():
    GPIO.output(TRIG,True)
    time.sleep(0.00001)        # 10uS의 펄스 발생을 위한 딜레이
    GPIO.output(TRIG, False)
        
    while GPIO.input(ECHO)==0:
        start = time.time()     # Echo핀 상승 시간값 저장
            
    while GPIO.input(ECHO)==1:
        stop = time.time()      # Echo핀 하강 시간값 저장
            
    check_time = stop - start
    distance = check_time * 34300 / 2
    print("Distance : %.1f cm" % distance)
    time.sleep(0.4)

def calculate_angle(h,r,distance):
    #h=계단높이
    #r=자동차 바퀴 반지름
    angle = math.atan(h / (r + distance))
    return angle

#서보모터 구동
#앞대가리 
def fd_up():
    angle=calculate_angle()
    set_servo_angle(servo_channels[4],angle) #서보(5) 올라갈준비
    set_servo_angle(servo_channels[5],angle) #서보(6) 올라갈준비
    time.sleep(1)

#중간
def md_up():
    angle=calculate_angle()/2 #angle의 반만 회전-무게때문에 
    set_servo_angle(servo_channels[2],angle) #서보(3) 올라갈준비
    set_servo_angle(servo_channels[3],angle) #서보(4) 올라갈준비
    time.sleep(1)


        
car = drivingclass()

def case_1():
    car.stop()   #일단 정지
    car.fd_up() #앞 대가리 올라갈 준비
    car.move_forward() # 2초간 전진
    time.sleep(2) # 2초간 전진
    car.md_up() # 반만회전
    move_forward() # 1초간 전진
    car.time.sleep(1) # 1초간 전진

def main():
    distance=get_distance()
    
    if distance<=3:
        case_1()
while True:
    car.goForward(1)
    time.sleep(1)
