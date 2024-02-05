"""
kdc101_example.py
=================

This example demonstrates basic control of the Thorlabs KDC101 DC motor controller using python.

It achieves control of the device via the Kinesis C API, interfaced with via ctypes. The example connects, homes, moves
and disconnects the device.

"""
import time
import os
import sys
from ctypes import *


def main():
    """
    main():
    ------

    Performs all actions of the KDC101
    :return: None
    """

    if sys.version_info < (3, 8):
        os.chdir(r"C:\Program Files\Thorlabs\Kinesis")
    else:
        os.add_dll_directory(r"C:\Program Files\Thorlabs\Kinesis")

    lib: CDLL = cdll.LoadLibrary("Thorlabs.MotionControl.KCube.DCServo.dll")

    # Uncomment this line if you are using simulations
    #lib.TLI_InitializeSimulations()

    # Set constants
    serial_num = c_char_p(b"27500125")

    # Open the device
    if lib.TLI_BuildDeviceList() == 0:
        lib.CC_Open(serial_num)
        lib.CC_StartPolling(serial_num, c_int(200))

        # Home the device
        lib.CC_Home(serial_num)
        time.sleep(1)

        # Set up the device to convert real units to device units
        STEPS_PER_REV = c_double(1919.64186)  # for the PRM1-Z8
        gbox_ratio = c_double(1.0)  # gearbox ratio
        pitch = c_double(1.0)

        # Apply these values to the device
        lib.CC_SetMotorParamsExt(serial_num, STEPS_PER_REV, gbox_ratio, pitch)

        # Get the device's current position in dev units
        lib.CC_RequestPosition(serial_num)
        time.sleep(0.2)
        dev_pos = c_int(lib.CC_GetPosition(serial_num))

        # Convert device units to real units
        real_pos = c_double()
        lib.CC_GetRealValueFromDeviceUnit(serial_num,
                                          dev_pos,
                                          byref(real_pos),
                                          0)

        print(f'Position after homing: {real_pos.value}')

        # set a new position in device units
        new_pos_real = c_double(5.0)  # in real units
        new_pos_dev = c_int()
        lib.CC_GetDeviceUnitFromRealValue(serial_num,
                                          new_pos_real,
                                          byref(new_pos_dev),
                                          0)

        print(f'{new_pos_real.value} in Device Units: {new_pos_dev.value}')

        # Move to new position as an absolute move.
        lib.CC_SetMoveAbsolutePosition(serial_num, new_pos_dev)
        time.sleep(0.25)
        lib.CC_MoveAbsolute(serial_num)

        # Close the device
        lib.CC_Close(serial_num)
    #.TLI_UninitializeSimulations()

    return


if __name__ == "__main__":
    main()
