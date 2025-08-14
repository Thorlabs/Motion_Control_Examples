# BBDXXX Examples
Software examples for Thorlabs' BBD series benchtop controllers

## BBD30X.py
This example uses the Kinesis C/C++ library and the Python module 'ctypes'´.

## bbd_pythonnet.py
This example uses the Kinesis .NET library and the Python module 'pythonNET'.


## BBD30x_Serial_Command_pySerial.py

This example uses serial commands as documented in the "APT Communications Protocol" and the Python module "pyserial". Please follow the following steps to setup a Virtual Communication Port for Windows OS. 
1. Power up the device and connect the device to the PC using the USB cable
2. Open the device manager by selecting Start/Control Panel/Device Manager/
3. Click ‘USB Serial Bus Controllers’ and select the APT USB Device to be configured, then right click and select ‘Properties’.
4. Select the ‘Advanced’ tab, and check the ‘Load VCP’ box.
5. Click OK, then power cycle the device being configured.
6. In the device manager, click ‘Ports (COM & LPT)’, and note the ‘APT USB Device Serial Port’ COM port number (e.g. COM3). This COM port can then be used for low level protocol messages.

