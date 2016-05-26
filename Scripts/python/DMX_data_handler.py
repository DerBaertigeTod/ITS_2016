import serial
from conf import *
#Initializing
ser = serial.Serial(
    port='/dev/ttyAMA0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

#FUNCTIONS


def build_array(channels=512, value=0, single=False):
    "Produces an array in either Hex or Decimal for each DMX Channel and returns it"
    _array[512] = 0
    if not single:
        for x in range(0, channels):
            _array[x] = value
    else:
        _array[channels] = value
    

    if kind == 'serial':
        for x in range(len(_array)):
            _array[x] = str(_array[x])
        return _array.join(',')
    else:
        for x in range(len(_array)):
            _array[x] = hex(_array[x])
        return _array




def send_serial_data(channels, value):
    "Sends a values to DMX channels via Serial"
    ser.write(build_array(channels, value, 'serial'))


def read_serial_data():
    "Reads the incomming Serial DATA"
    values = ser.readline()
    if values.startswith('['):
        dmx = values.split(',')
        return dmx
    else:
        return 0

