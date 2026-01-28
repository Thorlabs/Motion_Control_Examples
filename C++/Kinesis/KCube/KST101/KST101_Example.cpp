/*
KST101 Simple Example
Date of Creation(YYYY-MM-DD): 2021-12-24
Date of Last Modification on Github: 2022-09-21
C++ Version Used: ISO C++ 14
Kinesis Version Tested: 1.14.40
*/

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

// include device-specific header file
#include "Thorlabs.MotionControl.KCube.StepperMotor.h"


int __cdecl wmain(int argc, wchar_t* argv[])
{
	// Uncomment this line (and TLI_UnitializeSimulations at the bottom of the page)
	// If you are using a simulated device
	//TLI_InitializeSimulations();

	// Change this line to reflect your device's serial number
    int serialNo = 80000001;

    // Optionally set the position of the device (in device units)
    int position = 0;

	// Optionally set the velocity of the device (in device units/second)
    int velocity = 0;

    // identify and access device
    char testSerialNo[16];
    sprintf_s(testSerialNo, "%d", serialNo);

    // Build list of connected device
    if (TLI_BuildDeviceList() == 0)
    {
        // get device list size 
        short n = TLI_GetDeviceListSize();
        // get BBD serial numbers
        char serialNos[100];
        TLI_GetDeviceListByTypeExt(serialNos, 100, 80);

        // Search serial numbers for given serial number
        if (strstr(serialNos, testSerialNo)) {
            printf("Device %s found", testSerialNo);
        }
        else {
            printf("Device %s Not Found", testSerialNo);
            return -1;
        }

        // open device
        if(SCC_Open(testSerialNo) == 0)
        {
            // start the device polling at 200ms intervals
            SCC_StartPolling(testSerialNo, 200);

            Sleep(3000);
            // Home device
            SCC_ClearMessageQueue(testSerialNo);
            SCC_Home(testSerialNo);
            printf("Device %s homing\r\n", testSerialNo);

            // wait for completion
            WORD messageType;
            WORD messageId;
            DWORD messageData;
            SCC_WaitForMessage(testSerialNo, &messageType, &messageId, &messageData);
            while(messageType != 2 || messageId != 0)
            {
                SCC_WaitForMessage(testSerialNo, &messageType, &messageId, &messageData);
            }

            // set velocity if desired
            if(velocity > 0)
            {
                int currentVelocity, currentAcceleration;
                SCC_GetVelParams(testSerialNo, &currentAcceleration, &currentVelocity);
                SCC_SetVelParams(testSerialNo, currentAcceleration, velocity);
            }

            // move to position (channel 1)
            SCC_ClearMessageQueue(testSerialNo);
            SCC_MoveToPosition(testSerialNo, position);
            printf("Device %s moving\r\n", testSerialNo);

            // wait for completion
            SCC_WaitForMessage(testSerialNo, &messageType, &messageId, &messageData);
            while(messageType != 2 || messageId != 1)
            {
                SCC_WaitForMessage(testSerialNo, &messageType, &messageId, &messageData);
            }

            // get actual poaition
            int pos = SCC_GetPosition(testSerialNo);
            printf("Device %s moved to %d\r\n", testSerialNo, pos);

            // stop polling
            SCC_StopPolling(testSerialNo);
            // close device
            SCC_Close(testSerialNo);
        }
    }

	// Uncomment this line if you are using simulations
	//TLI_UnitializeSimulations;
    char c = _getch();
    return 0;
}
