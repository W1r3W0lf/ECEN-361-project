import sys
import RPi.GPIO as GPIO
sys.path.insert(0, '/home/pi/MiniTesla-Car/raspirobotboard3/python')
import time
from rrb3 import *

# set_motors(left motor speed, direction (0 forward or 1 backward), right motor speed, direction (0 forward or 1 backward)

#Steering motor connected to Left Motor on board
#    0 for left, 1 for right
#Drive motor connected to Right Motor on board
#    0 for forward, 1 for backward

#RRB3(battery voltage, motor output voltage)
rr = RRB3(6, 6)

def init_vehicle():
    rr.set_led1(1)

def turn_left(angle):
    
    rr.set_motors(1, 0, 0, 0)
    time.sleep(2.3*angle/360)
    #stop()

def turn_right(angle):
    rr.set_motors(1, 1, 0, 0)
    time.sleep(2.1*angle/360)
    #stop()

def forward(distance):
    rr.set_motors(0, 0, 1, 0)
    time.sleep(distance)
    stop()
    
def backward(distance):
    rr.set_motors(0, 0, 1, 1)
    time.sleep(distance)
    stop()

def stop():
    rr.set_motors(0, 0, 0, 0)
    time.sleep(.2)
    
def cleanup():
    GPIO.cleanup()

turn_left(90)
turn_right(90)
turn_left(30)
backward(1)
time.sleep(2)
forward(1)
cleanup()
