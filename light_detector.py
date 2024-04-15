# source: https://www.freva.com/fr/capteur-de-lumiere-photoresistance-avec-raspberry-pi/

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # define number of pins mode
GPIO.setwarnings(False) # to avoid warning messages

LIGHT_PIN = 23 # 8 pin on the first row

GPIO.setup(LIGHT_PIN, GPIO.IN) # set up the pin as an input one
lOld = not GPIO.input(LIGHT_PIN) # save last state of the sensor (used for comparison)
print('Starting up the LIGHT Module (click on STOP to exit)')

time.sleep(0.5) # wait for sensor stabilisation

while True:
  if GPIO.input(LIGHT_PIN) != lOld:
    if GPIO.input(LIGHT_PIN):
      print ('\u263e - dark')
    else:
      print ('\u263c - light') 
  lOld = GPIO.input(LIGHT_PIN)
  time.sleep(0.2)

