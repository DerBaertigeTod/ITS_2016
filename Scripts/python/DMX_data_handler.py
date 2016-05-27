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


def build_array(channels=512, value=0, kind='serial', single=False):
    "Produces an array for each DMX Channel"
    _array = range(512)
    kette = ""
    if not single:
        for x in range(0, channels):
            _array[x] = value
    else:
        _array[channels] = value

    if kind == 'serial':
        first = True
        for x in xrange(0, channels):
            _array[x] = str(_array[x])
            if first:
                kette = str(_array[x])
                first = False
        else:
                kette = kette+'&'+str(_array[x])
        return (kette+'\n').encode('ascii')


def send_serial_data(channels, value):
    "Sends a values to DMX channels via Serial"
    ser.write(chr(13).encode('ascii'))
    ser.write(build_array(channels, value, 'serial'))


def read_serial_data():
    "Reads the incomming Serial DATA"
    values = ser.readline()

    if (values != ""):
        dmx = values.split(',')
        return dmx
    else:
        emtpy = range(256)
        for y in emtpy:
            empty[y] = 0

        return emtpy
