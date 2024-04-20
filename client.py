# source: https://websockets.readthedocs.io/en/stable/
# import asyncio
from websockets.sync.client import connect

server_ip = "192.168.0.175"

def send_msg(data, port):
    with connect(f"ws://{server_ip}:{port}") as websocket: # works with channel of fbcop ✨
        websocket.send(data)

