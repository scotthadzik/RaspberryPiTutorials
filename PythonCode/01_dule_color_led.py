#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

PIN_R = 11

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(PIN_R, GPIO.OUT)   # Set the R pin to mode is output
GPIO.output(PIN_R, GPIO.HIGH)  # Set the R pin to High(5V) to turn on led
