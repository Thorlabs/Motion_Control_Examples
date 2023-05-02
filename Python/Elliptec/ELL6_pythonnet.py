#Example tested for ELL6
import sys, os, time
import clr


clr.AddReference('C:\Program Files\Thorlabs\Elliptec\Thorlabs.Elliptec.ELLO_DLL.dll')

from Thorlabs.Elliptec.ELLO_DLL import *
ELLDevicePort.Connect('COM4')#Check Windows Device Manager to find out which COM port is used

min_address="0"
max_address="F"

ellDevices=ELLDevices()
devices=ellDevices.ScanAddresses(min_address, max_address)


for device in devices:
    if ellDevices.Configure(device):
        
        addressedDevice=ellDevices.AddressedDevice(device[0])

        deviceInfo=addressedDevice.DeviceInfo
        for stri in deviceInfo.Description():
            print(stri)

        addressedDevice.Home(ELLBaseDevice.DeviceDirection.Linear)
        time.sleep(1)
        addressedDevice.JogForward()
        time.sleep(1)
        addressedDevice.JogBackward()
            
    
    


