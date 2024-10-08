# source: https://www.freva.com/fr/capteur-de-lumiere-photoresistance-avec-raspberry-pi/

import RPi.GPIO as GPIO
import time
import client

GPIO.setmode(GPIO.BCM) # define number of pins mode
GPIO.setwarnings(False) # to avoid warning messages

LIGHT_PIN = 14 # pin number 4 of the first row
port = "1111"

GPIO.setup(LIGHT_PIN, GPIO.IN) # set up the pin as an input one
# lOld = not GPIO.input(LIGHT_PIN) # save last state of the sensor (used for comparison)
print('Starting up the LIGHT Module (click on STOP to exit)')

time.sleep(0.5) # wait for sensor stabilisation

while True:
  # source: https://www.uugear.com/portfolio/using-light-sensor-module-with-raspberry-pi/
  sensor_value = GPIO.input(LIGHT_PIN)
  print ("LDR_out: " + str(sensor_value) )# 0: light
  client.send_msg(str(sensor_value), port)
  time.sleep(0.2)

