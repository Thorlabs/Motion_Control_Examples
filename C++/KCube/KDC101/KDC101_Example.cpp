// Example_KDC101.cpp : Defines the entry point for the console application.

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

// Include library specific header file
#include "Thorlabs.MotionControl.KCube.DCServo.h"


int __cdecl wmain(int argc, wchar_t* argv[])
{
    // Comment/uncomment this line based on whether or not you're using simulation.
	//TLI_InitializeSimulations();

	// Change this line to reflect your device's serial number
    int serialNo = 27000001; 

    // optionally set a position in device units.
    int position = 0;

	// Optionally change this value to a desired velocity (in device units/second)--*--+cx vc                                                                       
     int velocity = 0;

    // identify and access device
    char testSerialNo[16];
    sprintf_s(testSerialNo, "%d", serialNo);

    // Build list of connected device
    if (TLI_BuildDeviceList() == 0)
    {
        // get device list size 
        short n = TLI_GetDeviceListSize();
        // get KDC serial numbers
        char serialNos[100];
        TLI_GetDeviceListByTypeExt(serialNos, 100, 27);

        // output list of matching devices
		// This bit is optional and can largely be ignored.
        {
            char *searchContext = nullptr;
            char *p = strtok_s(serialNos, ",", &searchContext);

            while (p != nullptr)
            {
                TLI_DeviceInfo deviceInfo;
                // get device info from device
                TLI_GetDeviceInfo(p, &deviceInfo);
                // get strings from device info structure
                char desc[65];
                strncpy_s(desc, deviceInfo.description, 64);
                desc[64] = '\0';
                char serialNo[9];
                strncpy_s(serialNo, deviceInfo.serialNo, 8);
                serialNo[8] = '\0';
                // output
                printf("Found Device %s=%s : %s\r\n", p, serialNo, desc);
                p = strtok_s(nullptr, ",", &searchContext);
            }
        }

        // open device
        if(CC_Open(testSerialNo) == 0)
        {
            // start the device polling at 200ms intervals
            CC_StartPolling(testSerialNo, 200);

			// Home device
            CC_ClearMessageQueue(testSerialNo);
            CC_Home(testSerialNo);
            printf("Device %s homing\r\n", testSerialNo);

            // wait for completion
            WORD messageType;
            WORD messageId;
            DWORD messageData;
            CC_WaitForMessage(testSerialNo, &messageType, &messageId, &messageData);
            while(messageType != 2 || messageId != 0)
            {
                CC_WaitForMessage(testSerialNo, &messageType, &messageId, &messageData);
            }

            // set velocity if desired
            if(velocity > 0)
            {
                int currentVelocity, currentAcceleration;
                CC_GetVelParams(testSerialNo, &currentAcceleration, &currentVelocity);
                CC_SetVelParams(testSerialNo, currentAcceleration, velocity);
            }

            // move to position (channel 1)
            CC_ClearMessageQueue(testSerialNo);
            CC_MoveToPosition(testSerialNo, position);
            

            // stop polling
            CC_StopPolling(testSerialNo);
            // close device
            CC_Close(testSerialNo);
        }
    }

	// Uncomment this line if you are using simulations
	//TLI_UninitializeSimulations();

    char c = _getch();
    return 0;
}
