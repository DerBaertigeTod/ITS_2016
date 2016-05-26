import smbus
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
bus = smbus.SMBus(1)
#FUNCTIONS


def build_array(channels=512, value=0, single=False):
    "Produces an array in either Hex or Decimal for each DMX Channel and returns it"
    array = []
    if not single:
        for x in range(0, channels):
            array[x] = value
    else:
        array[channels] = value
    

    if kind == 'serial':
        for x in range(len(array)):
            array[x] = str(array[x])
        return array.join(',')
    else:
        for x in range(len(array)):
            array[x] = hex(array[x])
        return array




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


def read_i2c_data():
    "Reads the incomming I2C DATA"
    values = bus.read_i2c_block_data(
        conf.DEVICE_ADDRESS,
        conf.DEVICE_REG_DMX0_IN)
    for x in range(len(values)):
        dmx = values.split(',')
    return dmx
