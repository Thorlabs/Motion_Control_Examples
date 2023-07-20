# -*- coding: utf-8 -*-

import serial
import time

"""
Spyder Editor

This is a temporary script file.
"""


def main():
    com = serial.Serial(port='COM15',
                        baudrate=115200,
                        bytesize=8,
                        parity=serial.PARITY_NONE,
                        stopbits=1, xonxoff=0,
                        rtscts=0,
                        timeout=1
                        )

    print(com.is_open)
    com.flushInput()
    com.flushOutput()

    command = bytearray([0x05, 0x00, 0x00, 0x00, 0x01, 0x01])  # identify
    com.write(command)
    com.flushInput()
    com.flushOutput()
    time.sleep(1)

    com.write(bytearray([0x10, 0x02, 0x01, 0x01, 0x21, 0x01]))  # enable
    com.flushInput()
    com.flushOutput()
    time.sleep(1)

    com.write(bytearray([0x43, 0x04, 0x01, 0x00, 0x21, 0x01]))  # home
    com.flushInput()
    com.flushOutput()
    time.sleep(5)

    com.write(bytearray(
        [0x50, 0x04, 0x06, 0x00, 0xA1, 0x01, 0x01, 0x00, 0xC7, 0xB1, 0x00, 0x00]))  # setmove abs parameterMove to 5deg
    com.flushInput()
    com.flushOutput()
    time.sleep(4)

    com.write(bytearray([0x53, 0x04, 0x06, 0x00, 0x21, 0x01, 0x01, 0x00, 0x40, 0x0D, 0x03, 0x00]))  # moveAbs
    com.flushInput()
    com.flushOutput()
    time.sleep(4)

    com.write(bytearray([0x16, 0x04, 0x16, 0x00, 0xA1, 0x01  # header
                            , 0x01, 0x00, 0x02, 0x00  # Channel, JogMode
                            , 0x99, 0x99, 0x99, 0x00  # Step Size
                            , 0x00, 0x00, 0x00, 0x00  # Min Velocity
                            , 0xB0, 0x35, 0x00, 0x00  # Acelleration
                            , 0x9D, 0xCC, 0xCC, 0x00  # Max Velocity
                            , 0x02, 0x00]))  # Stop Mode   #set Jog Params
    com.flushInput()
    com.flushOutput()
    time.sleep(1)

    com.write(bytearray([0x6A, 0x04, 0x01, 0x01, 0x21, 0x01]))  # jog
    com.flushInput()
    com.flushOutput()

    com.close()
    print(com.is_open)


main()
