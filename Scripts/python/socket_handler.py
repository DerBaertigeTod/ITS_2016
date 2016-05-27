from conf import *
from DMX_data_handler import *
from socketIO_client import SocketIO


socketIO = SocketIO(SERVER, PORT)


def on_checkbox_response(*args):
        data = args[0]
        print data["value"]


def send_dmx_channel(*arguments):
    "Sends DMX Channel range"
    send_serial_data(10, 0)
    print "something should happen"


def send_websocket(which, *data):
    "Sends data trough Websocket on 'which' call"
    socketIO.emit(which, {'data': data})


def receive_websockets():
    "Collects Websocket data and calls the right function"
#    socketIO.on('slider1', slider1_call)
    socketIO.on('checkbox', send_dmx_channel)
    socketIO.wait()
