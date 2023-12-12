"""
Example KDC101_serial.py
Example Date of Creation: 2023-12-12
Example Date of Last Modification on Github: 2023-12-12
Version of Python used for Testing: 3.11.4
==================
Example Description: The example shows how to connect to KDC101 on Windows and Linux. The motor is homed and moved 1 mm
Tested with KDC101 and Z812 
"""


import serial
import time

def main():

    #open serial port

    #For Windows
    #find out COM port number in the Device Manager and adapt the following line
    ser=serial.Serial(port='COM4',baudrate=115200,bytesize=8,
                      parity=serial.PARITY_NONE,
                      stopbits=1,xonxoff=0,
                      rtscts=0,
                      timeout=1)

    #For Linux
    # use 'dmesg | grep tty' to find serial port
    # eventually need to change permissions for /dev/tty*
    # uncomment the following lines
##    ser=serial.Serial('/dev/ttyUSB0', baudrate=115200,bytesize=8,
##                      parity=serial.PARITY_NONE,
##                      stopbits=1,xonxoff=0,
##                      rtscts=0,
##                      timeout=1)  



    print(ser.is_open)
    ser.flushInput()
    ser.flushOutput()

    command = bytearray([0x23, 0x02, 0x00, 0x00, 0x50, 0x01])  # MGMSG_MOD_IDENTIFY
    ser.write(command)
    ser.flushInput()
    ser.flushOutput()
    time.sleep(1)

    ser.write(bytearray([0x10, 0x02, 0x01, 0x01, 0x50, 0x01]))  # MGMSG_MOD_SET_CHANENABLESTATE
    ser.flushInput()
    ser.flushOutput()
    time.sleep(1)

    ser.write(bytearray([0x43, 0x04, 0x01, 0x00, 0x50, 0x01]))  # MGMSG_MOT_MOVE_HOME
    ser.flushInput()
    ser.flushOutput()
    time.sleep(5)

    ser.write(bytearray(
        [0x53, 0x04, 0x06, 0x00, 0xD0, 0x01, 0x01, 0x00, 0xFB, 0x86, 0x00, 0x00]))  # MGMSG_MOT_MOVE_ABSOLUTE 1 mm
    ser.flushInput()
    ser.flushOutput()
    time.sleep(4)


    ser.close()

if __name__ == "__main__":
    main()


