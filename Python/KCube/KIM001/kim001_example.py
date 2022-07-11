from .kim001 import *

import time

test_serial_no = '85837825'

if TLI_BuildDeviceList() == 0:
    # get device list size
    n = TLI_GetDeviceListSize()
    
    # get serial numbers in device list
    serial_nos = TLI_GetDeviceListExt()
    
    # print description of each device
    for serial_no in serial_nos:
        info = TLI_GetDeviceInfo(serial_no)
        print(f"Found device {serial_no}={info.serialNo} : {info.description}")
    
    # open device
    if KIM_Open(test_serial_no) == 0:
        # poll at 200 ms intervals
        KIM_StartPolling(test_serial_no, 200)
        
        time.sleep(1.0)
        
        # initialize current position to zero
        KIM_SetPosition(test_serial_no, KIM_Channels.Channel1, 0)
        
        # Move to
        KIM_MoveAbsolute(test_serial_no, KIM_Channels.Channel1, 1000)
        time.sleep(0.2)
        print(f"Device {test_serial_no} moving to 1000")
        time.sleep(5.0)
        
        pos = KIM_GetCurrentPosition(test_serial_no, KIM_Channels.Channel1)
        print(f"Device {test_serial_no} position is {pos}")
        
        # Move Jog
        KIM_MoveJog(test_serial_no, KIM_Channels.Channel1, KIM_TravelDirection.Forward)
        time.sleep(0.2)
        print(f"Device {test_serial_no} jogging")
        time.sleep(2.0)
        
        pos = KIM_GetCurrentPosition(test_serial_no, KIM_Channels.Channel1)
        print(f"Device {test_serial_no} position is {pos}")
        
        # stop polling
        KIM_StopPolling(test_serial_no)
        
        # close device
        KIM_Close(test_serial_no)