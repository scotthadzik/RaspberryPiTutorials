#!/usr/bin/env python
import RPi.GPIO as GPIO

PIN_R = 12

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(PIN_R, GPIO.OUT)   # Set the R pin to mode is output


while True:
    GPIO.output(PIN_R, GPIO.HIGH)  # Set the R pin to High(3.3V) to turn on led
