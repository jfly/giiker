# Copied and modified from https://github.com/xbmc/xbmc/blob/master/tools/EventClients/examples/python/example_button1.py

import urllib.request
import json
import threading
from socket import *
import queue
import time

from xbmcclient import *

class KodiEventClient():
    def __init__(self):
        # connect to localhost, port 9777 using a UDP socket
        # this only needs to be done once.
        # by default this is where XBMC will be listening for incoming
        # connections.
        host = "clark"
        port = 9777
        self._addr = (host, port)
        self._sock = socket(AF_INET,SOCK_DGRAM)

        packet = PacketHELO(devicename="Giiker Cube", icon_type=ICON_PNG, icon_file="333.png")
        packet.send(self._sock, self._addr)

        self._packet_queue = queue.Queue()
        self._stopper = threading.Event()
        self._thread = threading.Thread(target=self._thread)
        self._thread.start()

    def _thread(self):
        while not self._stopper.is_set():
            try:
                packet = self._packet_queue.get(block=True, timeout=3.0)
            except queue.Empty:
                packet = PacketPING()

            packet.send(self._sock, self._addr)

        packet = PacketBYE()
        packet.send(self._sock, self._addr)
        del self._sock
                
    def press_button(self, button_name):
        packet = PacketBUTTON(map_name="KB", button_name=button_name, repeat=0, queue=1)
        packet.send(self._sock, self._addr)

    def send_notification(self, caption, message):
        packet = PacketNOTIFICATION(caption, message, ICON_PNG, "333.png")
        packet.send(self._sock, self._addr)

    def close(self):
        self._stopper.set()
        self._thread.join()

def json_rpc(method, params=[]):
    data = [{
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 4242,
    }]
    req = urllib.request.Request('http://xbmc.clark.jflei.com/jsonrpc',
                                 data=json.dumps(data).encode('utf8'),
                                 headers={'content-type': 'application/json'})
    urllib.request.urlopen(req)

def main():
    client = KodiEventClient()
    client.press_button("down")
    client.close()

if __name__=="__main__":
    main()
