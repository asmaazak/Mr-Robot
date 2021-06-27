from gpiozero import Motor, LineSensor, Buzzer, MotionSensor, spidev
import gpiozero as GPIO

from signal import pause
from time import sleep
from picamera import PiCamera
from datetime import datetime

camera = PiCamera()
gas = GPIO.input(14)
pir1 = MotionSensor(15)
pir2 = MotionSensor(18)
left_sensor = LineSensor(3)
right_sensor = LineSensor(4)
buzz = Buzzer(2)
motorA = Motor(19, 13)
motorB = Motor(6, 5)
motorC = Motor(20, 16)
motorD = Motor(12, 7)
ir1 = spidev(17)
ir2 = spidev(27)
ir3 = spidev(22)
ir4 = spidev(10)

filename = "{0:%Y}-{0:%m}-{0:%d}".format(datetime.now())


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gas, GPIO.IN)
    GPIO.setup(Buzzer, GPIO.OUT)
    GPIO.setwarnings(False)


def forward():
    motorA.forward()
    motorB.forward()
    motorC.forward()
    motorD.forward()


def backward():
    motorA.backward()
    motorB.backward()
    motorC.backward()
    motorD.backward()


def right():
    motorA.backward()
    motorB.forward()
    motorC.forward()
    motorD.backward()


def left():
    motorA.forward()
    motorB.backward()
    motorC.backward()
    motorA.forward()


def upper_right():
    motorB.forward()
    motorC.forward()


def upper_left():
    motorA.forward()
    motorD.forward()


def lower_right():
    motorB.backward()
    motorC.backward()


def lower_left():
    motorA.backward()
    motorD.backward()


def rotate_left():
    motorA.forward()
    motorB.backward()
    motorC.forward()
    motorD.backward()


def rotate_right():
    motorA.backward()
    motorB.forward()
    motorC.backward()
    motorD.forward()

def stop():
    motorA.stop()
    motorB.stop()
    motorC.stop()
    motorD.stop()


def loop():
    while True:
        pir1.wait_for_motion()
        pir2.wait_for_motion()
        gas()

        Buzzer.on()
        sleep(1.5)
        Buzzer.off()
        sleep(0.5)
        camera.start_recording(filename)
        sleep(300)



        pause()

