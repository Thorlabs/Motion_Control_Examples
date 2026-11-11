"""
ELL20 serial Example
Date of Creation(YYYY-MM-DD): 2026-23-09
Date of Last Modification on Github: 2026-23-09
Python Version Used: Python 3.13
The example shows how to connect to a ELL20 stage, home and jog using Pyserial.
Tested on Windows 11 and Linux Mint 22.2

"""

import serial
import time

print("Connecting...")
com = serial.Serial(port = 'COM4',   #Windows: Change COM port according to device manager. Linux: e.g. '/dev/ttyUSB0'
                        baudrate = 9600,
                        bytesize=8,
                        parity=serial.PARITY_NONE,
                        stopbits=1, xonxoff=0,
                        rtscts=0,
                        timeout=1
    )
 
time.sleep(1)
 
com.flushInput()
com.flushOutput()

print("Scanning addresses...")
for i in range(0,15):
    com.write(bytearray(str.encode(str(hex(i))+'in','utf-8')))
    data=com.readline()
    print(hex(i), data.decode())
    if data.decode() !='':
        addr=hex(i)
        print("Adress is", addr)

print("Home and move") 
com.write(bytearray(str.encode(str(addr)+'ho0','utf-8')))#home
time.sleep(1)
com.write(bytearray(str.encode(str(addr)+'fw','utf-8')))#jog forward
time.sleep(1)
com.write(bytearray(str.encode(str(addr)+'bw','utf-8')))#jog backwards 

com.close
print("Connection closed")

 
