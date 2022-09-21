// Example_KBD101.cpp : Defines the entry point for the console application.
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

// Import device-specific header file
#include "Thorlabs.MotionControl.KCube.BrushlessMotor.h"


int __cdecl wmain(int argc, wchar_t* argv[])
{
	// Uncomment this line (and TLI_UnitializeSimulations() at the bottom of the page)
	// if you are using a simulated device
	//TLI_InitializeSimulations();
    
	// Change the serial number to match the one found on your device
    int serialNo = 28000001;

    // optionally set a position in device units.
    int position = 0;

	// Optionally set a velocity in terms of device units/second
    int velocity = 0;

    // identify and access device
    char testSerialNo[16];
    sprintf_s(testSerialNo, "%d", serialNo);

    // Build list of connected devices
    if (TLI_BuildDeviceList() == 0)
    {
        // get device list size 
        short n = TLI_GetDeviceListSize();

        // get KBD serial numbers
        char serialNos[100];
        TLI_GetDeviceListByTypeExt(serialNos, 100, 28); // Third input is device prefix

                // Search serial numbers for given serial number
        if (strstr(serialNos, testSerialNo)) {
            printf("Device %s found", testSerialNo);
        }
        else {
            printf("Device %s Not Found", testSerialNo);
            return -1;
        }

        // open device
        if(BMC_Open(testSerialNo) == 0)
        {
            // start the device polling at 200ms intervals
            BMC_StartPolling(testSerialNo, 200);

            // enable device so that it can move
            BMC_EnableChannel(testSerialNo);

            Sleep(1000);
            // Home device
            BMC_ClearMessageQueue(testSerialNo);
            BMC_Home(testSerialNo);

            printf("Device %s homing\r\n", testSerialNo);

            WORD messageType;
            WORD messageId;
            DWORD messageData;

			// Wait to receive message from device that it has home
			// Refer to the Messages section of the C API for more information on messageType and messageID
            BMC_WaitForMessage(testSerialNo, &messageType, &messageId, &messageData);
            while(messageType != 2 || messageId != 0)
            {
                BMC_WaitForMessage(testSerialNo, &messageType, &messageId, &messageData);
            }

            // set velocity if desired
            if(velocity > 0)
            {
                int currentVelocity, currentAcceleration;
                BMC_GetVelParams(testSerialNo, &currentAcceleration, &currentVelocity);
                BMC_SetVelParams(testSerialNo, currentAcceleration, velocity);
            }

            // move to position (channel 1)
            BMC_ClearMessageQueue(testSerialNo);
            BMC_MoveToPosition(testSerialNo, position);
            printf("Device %s moving\r\n", testSerialNo);

            // wait for completion
			BMC_WaitForMessage(testSerialNo, &messageType, &messageId, &messageData);
			// messageType 2: Generic Motor.
			// messageID 1: Move complete.
            while(messageType != 2 || messageId != 1)
            {
                BMC_WaitForMessage(testSerialNo, &messageType, &messageId, &messageData);
            }

            // get actual position
            int pos = BMC_GetPosition(testSerialNo);
            printf("Device %s moved to %d\r\n", testSerialNo, pos);

            // stop polling
            BMC_StopPolling(testSerialNo);
            // close device
            BMC_Close(testSerialNo);
        }
    }

	// Uncomment this line if you are using simulated devices
	//TLI_UninitializeSimulations();
    char c = _getch();
    return 0;
}
