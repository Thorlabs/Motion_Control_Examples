/*
KDC101 Simple Example
Date of Creation(YYYY-MM-DD): 2021-12-24
Date of Last Modification on Github: 2022-09-21
C++ Version Used: ISO C++ 14
Kinesis Version Tested: 1.14.40
*/

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

        // Search serial numbers for given serial number
        if (strstr(serialNos, testSerialNo)) {
            printf("Device %s found", testSerialNo);
        }
        else {
            printf("Device %s Not Found", testSerialNo);
            return -1;
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
