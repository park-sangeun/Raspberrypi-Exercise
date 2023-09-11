from time import sleep
from adafruit_servokit import ServoKit

# ServoKit 객체 생성
kit = ServoKit(channels=16)

# 서보모터 0번 채널의 각도를 설정하는 함수
def set_servo_angle(channel, angle):
    kit.servo[channel].angle = angle

# 서보모터를 0도부터 180도까지 이동시키는 함수
def sweep_servo():
    set_servo_angle(2, 0)  # 서보모터를 0도로 초기화
    sleep(1)  # 1초 대기


def fd():
    set_servo_angle(0, 90)
    set_servo_angle(1, 90)
    sleep(1)

def md():
    set_servo_angle(2, 90)
    set_servo_angle(3, 90)
    sleep(1)



fd()
sleep(1)


# # set_servo_angle(2, 40)  # 서보모터를 180도로 이동
# sleep(1)  # 3초 대기
# set_servo_angle(2, 180)  # 서보모터를 180도로 이동
# sleep(1)  # 3초 대기
# set_servo_angle(2, 20)  # 서보모터를 180도로 이동
# sleep(1)  # 3초 대기
# set_servo_angle(2, 30)  # 서보모터를 180도로 이동
# sleep(1)  # 3초 대기
# set_servo_angle(3, 90)
# sleep(1)  # 3초 대기
# set_servo_angle(3, 10)  # 서보모터를 180도로 이동
# sleep(1)  # 3초 대기
# set_servo_angle(3, 20)  # 서보모터를 180도로 이동
# sleep(1)  # 3초 대기
# set_servo_angle(3, 30)  # 서보모터를 180도로 이동
# sleep(1)  # 3초 대기

