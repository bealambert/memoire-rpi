import client

port = "1113"

# source: https://github.com/israel-dryer/Raspberry-Pi-Sensors/blob/master/ds18b20_single.py
import os
import glob
import time

# these two lines mount the device:
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_path = glob.glob(base_dir + '28*')[0] # get file path of sensor
rom = device_path.split('/')[-1] # get rom name

def read_temp_raw():
    with open(device_path +'/w1_slave','r') as f:
        valid, temp = f.readlines()
    return valid, temp
 
def read_temp():
    valid, temp = read_temp_raw()

    while 'YES' not in valid:
        time.sleep(0.2)
        valid, temp = read_temp_raw()

    pos = temp.index('t=')
    if pos != -1:
        #read the temperature .
        temp_string = temp[pos+2:]
        temp_c = float(temp_string)/1000.0 
        return temp_c


while True:
    c = read_temp()
    print('DS18B20_out: C={:,.3f}'.format(c))
    client.send_msg(str(c), port)
    time.sleep(1)

