import serial
import sys
try:
    from xmodem import XMODEM
except ImportError:
    raise Exception('XMODEM module not found. Run "pip install xmodem" in powershell or terminal!')

## Parameters from the development platform
PORT_PATH = sys.argv[1] # Path to the serial port (ex. COM* on Windows or /dev/ttyUSB* on Linux)
MCU_TYPE = sys.argv[2] # MCU type defined when the bootloader flashed (ex. "F411RC")
BIN_PATH = sys.argv[3] # Path to the binary file (ex. firmware.bin)

## Parameters set by the bootloader design
BAUDRATE = 250000
HARDWARE_FLOW_CONTROL = False

## Some constants 
BEL = b'\x07'
ACK = b'\x06'
NAK = b'\x15'

# Define serial port and functions for XMODEM stream
port = serial.Serial(PORT_PATH, timeout=1, baudrate=BAUDRATE, rtscts=HARDWARE_FLOW_CONTROL)
port.open()

def getc(size, timeout=1):
    return port.read(size) or None

def putc(data, timeout=1):
    return port.write(data)

# Create modem and open firmware file
modem = XMODEM(getc, putc)
binary_stream = open(BIN_PATH, 'rb')

# Loop: Reset MCU and wait for BEL from serial port
# Break: BEL received
print('Resetting MCU and waiting for BEL')
while True: 
    # Reset MCU by toggling DTR
    port.dtr = 0
    port.dtr = 1
    ser_data = port.read(1)
    if ser_data.startswith(BEL):
        # Send ACK when BEL is received
        port.write(ACK)
        print('BEL receieved. Requesting to enter bootloader.')
        break

# Match MCU type
# Match: Send ACK
# No match: Send NAK and raise error
ser_data = port.read(6)
if ser_data.startswith(bytes(MCU_TYPE)):
    port.write(ACK)
    print('Correct MCU target. Sent ACK.')
else:
    port.write(NAK)
    raise('Incorrect MCU target. Sent NAK.')

# Loop: Wait for C from serial port ( after MCU clears it's user application space )
print('Waiting for MCU to erase application partition', end='')
while True:
    ser_data = port.read()
    if ser_data.startswith(b'C'):
        print()
        print('Uploading firmware!')
        break
    print('.', end='')

# Begin XMODEM transfer
modem.send(binary_stream)