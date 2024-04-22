# source: https://projects.raspberrypi.org/en/projects/physical-computing/11

from gpiozero import MotionSensor
# documentation: https://gpiozero.readthedocs.io/en/stable/api_input.html
from datetime import datetime
import client
import time

port = "1115"

pir = MotionSensor(15)

while True:
    print("PIR_out: Listen...")
    pir.wait_for_motion()
    t = datetime.timestamp(datetime.now())
    print(f"PIR_out: You moved at:{str(t)}")
    # time.sleep(1)
    client.send_msg(str(t), port)