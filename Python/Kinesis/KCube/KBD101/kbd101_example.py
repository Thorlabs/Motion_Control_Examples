"""
kbd101_example.py
=================

This example demonstrates basic control of the Thorlabs KBD101 Brushless motor controller using python.

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

    Performs all actions of the KBD101
    :return: None
    """

    if sys.version_info < (3, 8):
        os.chdir(r"C:\Program Files\Thorlabs\Kinesis")
    else:
        os.add_dll_directory(r"C:\Program Files\Thorlabs\Kinesis")

    lib: CDLL = cdll.LoadLibrary("Thorlabs.MotionControl.KCube.BrushlessMotor.dll")


    # Uncomment this line if you are using simulations
    #lib.TLI_InitializeSimulations()

    serial_num = c_char_p(b"00000000")

    # Open the device.
    if lib.TLI_BuildDeviceList() == 0: 
        lib.BMC_Open(serial_num)
        lib.BMC_StartPolling(serial_num, c_int(200))

        # Home the device
        lib.BMC_Home(serial_num)
        time.sleep(1)

        # Set up the device to convert real units to device units
        STEPS_PER_REV = c_double(1919.64186)  
        gbox_ratio = c_double(1.0)  
        pitch = c_double(1.0)

        # Get the device's current position in dev units
        lib.BMC_RequestPosition(serial_num)
        time.sleep(0.2)
        dev_pos = c_int(lib.BMC_GetPosition(serial_num))

        # Convert device units to real units
        real_pos = c_double()
        lib.BMC_GetRealValueFromDeviceUnit(serial_num,
                                          dev_pos,
                                          byref(real_pos),
                                          0)

        print(f'Position after homing: {real_pos.value}')

        # set a new position in device units
        new_pos_real = c_double(5.0)  # in real units
        new_pos_dev = c_int()
        lib.BMC_GetDeviceUnitFromRealValue(serial_num,
                                          new_pos_real,
                                          byref(new_pos_dev),
                                          0)

        print(f'{new_pos_real.value} in Device Units: {new_pos_dev.value}')

        # Move to new position as an absolute move.
        lib.BMC_SetMoveAbsolutePosition(serial_num, new_pos_dev)
        time.sleep(0.25)
        lib.BMC_MoveAbsolute(serial_num)

        # Close the device
        lib.BMC_Close(serial_num)

        # lib.TLI_UninitializeSimulations()
    return


if __name__ == "__main__":
    main()
