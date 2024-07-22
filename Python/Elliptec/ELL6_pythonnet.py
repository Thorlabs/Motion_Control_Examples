"""
ELL6 pythonnet Example
Date of Creation(YYYY-MM-DD): 2024-05-02
Date of Last Modification on Github: 2024-05-11
Python Version Used: python 3.10.5
ELLO Software Version: 1.6.2.0

"""
import sys, os, time
import clr


clr.AddReference('C:\Program Files\Thorlabs\Elliptec\Thorlabs.Elliptec.ELLO_DLL.dll')

from Thorlabs.Elliptec.ELLO_DLL import *

print("Initializing and enabling device, this might take a couple seconds...")

# Connect to device,check Windows Device Manager to find out which COM port is used.
ELLDevicePort.Connect('COM4')

# Define byte address. 
min_address="0"
max_address="F"

# Build device list.
ellDevices=ELLDevices()
devices=ellDevices.ScanAddresses(min_address, max_address)

# Initialize device. 
for device in devices:
    if ellDevices.Configure(device):
        
        addressedDevice=ellDevices.AddressedDevice(device[0])

        deviceInfo=addressedDevice.DeviceInfo
        for stri in deviceInfo.Description():
            print(stri)

        
        # Call move methods. 
        addressedDevice.Home(ELLBaseDevice.DeviceDirection.Linear)
        time.sleep(1)
        addressedDevice.JogForward()
        time.sleep(1)
        addressedDevice.JogBackward()
            
    
    


