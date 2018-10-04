#!/usr/bin/env python
import RPi.GPIO as GPIO

LED_PIN_R = 12 
BtnPinS = 11

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
GPIO.setup(LED_PIN_R, GPIO.OUT)   # Set the R pin to mode is output
GPIO.setup(BtnPinS, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BUTTON_PIN_S's mode is input, and pull up to high level(3.3V)


try:
    while True:
        GPIO.output(LED_PIN_R, GPIO.HIGH)  # Set the R pin to High(3.3V) to turn on led
except KeyboardInterrupt: #This is looking for a CTL+C
    GPIO.cleanup() #clean up the GPIO when exiting
