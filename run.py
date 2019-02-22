import time 
import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

PIN_SWITCHER_MOTOR = 26

PIN_MOTORS_LEFT_FORWARD = 17 
PIN_MOTORS_LEFT_BACK = 4
PIN_MOTORS_RIGHT_FORWARD = 22
PIN_MOTORS_RIGHT_BACK = 27

disablePins = [PIN_MOTORS_LEFT_FORWARD, PIN_MOTORS_LEFT_BACK, PIN_MOTORS_RIGHT_FORWARD, PIN_MOTORS_RIGHT_BACK, PIN_SWITCHER_MOTOR]
for pin in disablePins:
    GPIO.setup(pin, GPIO.OUT)  

for pin in disablePins:
   GPIO.output(pin, GPIO.LOW)  

def switchMotors(x): 
    GPIO.output(PIN_SWITCHER_MOTOR, x)

def enablePinsForTime(pins, sec):
    for pin in pins: 
        GPIO.output(pin, GPIO.HIGH) 
    time.sleep(sec) 
    for pin in pins: 
        GPIO.output(pin, GPIO.LOW) 
    time.sleep(0.5) 

def nazad(x):
    enablePinsForTime([PIN_MOTORS_LEFT_BACK, PIN_MOTORS_RIGHT_BACK], x)
 
def vpered(x):  
    enablePinsForTime([PIN_MOTORS_LEFT_FORWARD, PIN_MOTORS_RIGHT_FORWARD], x) 

def vlevo(x): 
    enablePinsForTime([PIN_MOTORS_RIGHT_BACK, PIN_MOTORS_LEFT_FORWARD], x)  
 
def vpravo(x):  
    enablePinsForTime([PIN_MOTORS_LEFT_BACK, PIN_MOTORS_RIGHT_FORWARD], x)  
   
switchMotors(1)
vpered(0.2)
nazad(0.2)
vlevo(1)
vpravo(1)
switchMotors(0) 
