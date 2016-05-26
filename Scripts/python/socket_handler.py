from conf import *
from socketIO_client import SocketIO


socketIO = SocketIO(conf.SERVER, conf.PORT)


def on_checkbox_response(*args):
        data = args[0]
        print data["value"]


def send_dmx_channel(*arguments):
    "Sends DMX Channel range"


def send_websocket(which, *data):
    "Sends data trough Websocket on 'which' call"
    socketIO.emit(which, {'data': data})


def receive_websockets():
    "Collects Websocket data and calls the right function"
    socketIO.on('slider1', slider1_call)
    socketIO.on('dmx_send_channel', send_dmx_channel)
    socketIO.waiit()

