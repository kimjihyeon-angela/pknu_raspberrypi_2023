# ServoMotor 테스트
import RPi.GPIO as GPIO
import time

pwm_pin = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwm_pin, GPIO.OUT)
pwm = GPIO.PWM(pwm_pin, 100)
angle = 3
pwm.start(angle)

while(True):
    cmd = input('키 입력 [f|r]')
    direction = cmd[0]
    if direction == 'f': # forward 순방향
        angle += 1
    else: # 'r' => reward 역방향
        angle -= 1

    if angle < 3 : # 최소 각도 : 3
        angle = 3
    elif angle > 20: 
        angle = 20 # 최대 각도 : 20

    print(f'angle = {(angle-3)*10}')
    pwm.ChangeDutyCycle(angle)