# source: https://projects.raspberrypi.org/en/projects/physical-computing/11

from gpiozero import MotionSensor
# documentation: https://gpiozero.readthedocs.io/en/stable/api_input.html
from datetime import datetime
import client

port = "1114"

pir = MotionSensor(23)

while True:
    print("Listen...")
    pir.wait_for_motion()
    t = datetime.timestamp(datetime.now())
    print(f"You moved at:{str(t)}")
    client.send_msg(str(t), port)