import time 
import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
  
PIN_SWITCHER_MOTOR = 26;         # пины: включение/выключение моторов  
PIN MOTOR_LEFT_FORWARD = 17      #       вращение левой оси вперёд 
PIN MOTOR_LEFT_BACK = 4          #                левой оси назад
PIN MOTOR_RIGHT_FORWARD = 22     #                правой оси вперёд
PIN MOTOR_RIGHT_BACK = 27        #                правой оси назад

#помечаем пины управления колёсами на вывод
disablePins = [MOTOR_LEFT_BACK, MOTOR_LEFT_FORWARD, MOTOR_RIGHT_BACK, MOTOR_RIGHT_FORWARD, PIN_SWITCHER_MOTOR]
for pin in disablePins:
    GPIO.setup(pin, GPIO.OUT)  

#гасим эти пины
for pin in disablePins:
   GPIO.output(pin, GPIO.LOW)  

#включение выключение моторов
def switchMotors(x): 
    GPIO.output(PIN_SWITCHER_MOTOR, x);

#включам пины pins на time секунд
def enablePinsForTime(pins, time):
    for pin in pins:
        GPIO.output(pin, GPIO.HIGH) 
    time.sleep(x) 
    for pin in pins:
        GPIO.output(pin, GPIO.LOW) 

def nazad(x): 
    enablePinsForTime([MOTOR_LEFT_BACK, MOTOR_RIGHT_BACK], x)
 
def vpered(x):  
    enablePinsForTime([MOTOR_LEFT_FORWARD, MOTOR_RIGHT_FORWARD], x) 

def vpravo(x): 
    enablePinsForTime([MOTOR_RIGHT_BACK, MOTOR_LEFT_FORWARD], x)  
 
def vlevo(x):  
    enablePinsForTime([MOTOR_LEFT_BACK, MOTOR_RIGHT_FORWARD], x)  
  

#test
switchMotors(true)
vpered(0.2)
time.sleep(1)
nazad(0.4)
time.sleep(1) 
vlevo(0.2)
time.sleep(1)  
vpravo(0.3)
time.sleep(1)  
vlevo(1)
Vpered(0.1)
