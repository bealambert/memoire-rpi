# source: https://projects.raspberrypi.org/en/projects/physical-computing/11

from gpiozero import MotionSensor
# documentation: https://gpiozero.readthedocs.io/en/stable/api_input.html
from datetime import datetime
import client
import RPi.GPIO as GPIO

port = "1114"

GPIO.setwarnings(False)

pir = MotionSensor(23)

while True:
    print("PIR_in: Listen...")
    pir.wait_for_motion()
    t = datetime.timestamp(datetime.now())
    print(f"PIR_in: You moved at:{str(t)}")
    # client.send_msg(str(t), port)