from socket_handler import *
from gpiozero import LED, Button
from time import sleep
reset = LED(12)

reset.off()
reset.on()
sleep(1)

receive_websockets();

