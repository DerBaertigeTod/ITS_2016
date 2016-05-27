from conf import *
from DMX_data_handler import *
from socketIO_client import SocketIO


socketIO = SocketIO(SERVER, PORT)


def on_checkbox_response(*args):
        data = args[0]
        print data["value"]


def send_dmx_channels(*arguments):
    "Sends DMX Channel range to 0"
    send_serial_data(256, 0)
    print "something should happen"


def send_dmx_channels_with_values(*data):
    "Sends DMX Channel range"
    send_serial_data(10, 'data': values)
    print "something should happen"


def send_websocket(which, *data):
    "Sends data trough Websocket on 'which' call"
    socketIO.emit(which, {'data': data})


def get_channel_values():
    "Sends receiving_channel values via broadcast"
    socketIO.broadcast.emit('channel_l', {'all': read_serial_data()})


def receive_websockets():
    "Collects Websocket data and calls the right function"
#    socketIO.on('slider1', slider1_call)
    socketIO.on('checkbox', send_dmx_channels)
    socketIO.on('lampe', send_dmx_channel_with_values)
    socketIO.on('get_channels', get_channel_values)
    socketIO.wait()
