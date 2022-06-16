"""
template.py
=================

This page is intended as a template for the creation of motion control programs written in python.

In this file, only functions common to all devices are shown. The rest must be filled out.

The intention is for all examples to conform to the PEP8 standard: https://peps.python.org/pep-0008/

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

    lib: CDLL = cdll.LoadLibrary("")

    # Uncomment this line if you are using simulations
    lib.TLI_InitializeSimulations()

    # Set constants
    serial_num = c_char_p(b"")

    # Open the device
    if lib.TLI_BuildDeviceList() == 0:

        ...

    # Uncomment this line if you are using simulations
    lib.TLI_UninitializeSimulations()

    return None


if __name__ == "__main__":
    main()
