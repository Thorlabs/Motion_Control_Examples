// Example_BDC103.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

#include "Thorlabs.MotionControl.Benchtop.DCServo.h"
int __cdecl wmain(int argc, wchar_t* argv[])
{
	// Uncomment this line (and TLI_UnitializeSimulations at the bottom of the page)
	// If you are using a simulated device
	//TLI_InitializeSimulations();

	// Change this line to reflect your device's serial number
	int serialNo = 43000001;
	
	// Optionally set the position (in device units)
	int position = 0;

	// Optionally set the velocity (in device units per second)
	int velocity = 0;
	
	// identify and access device
	char testSerialNo[16];
	sprintf_s(testSerialNo, "%d", serialNo);

	// Build list of connected device
    if (TLI_BuildDeviceList() == 0)
    {
		// get device list size 
        short n = TLI_GetDeviceListSize();
		// get BDC serial numbers
        char serialNos[100];
		
		TLI_GetDeviceListByTypeExt(serialNos, 100, 43);

		// Search serial numbers for given serial number
		if (strstr(serialNos, testSerialNo)) {
			printf("Device %s found", testSerialNo);
		}
		else {
			printf("Device %s Not Found", testSerialNo);
			return -1;
		}

		// open device
		if(BDC_Open(testSerialNo) == 0)
		{
			// start the device polling at 200ms intervals
			BDC_StartPolling(testSerialNo, 1, 200);

			// enable device so that it can move
			BDC_EnableChannel(testSerialNo, 1);

			Sleep(3000);
			// Home device
			BDC_ClearMessageQueue(testSerialNo, 1);
			BDC_Home(testSerialNo, 1);
			printf("Device %s homing\r\n", testSerialNo);

			// wait for completion
			WORD messageType;
			WORD messageId;
			DWORD messageData;
			BDC_WaitForMessage(testSerialNo, 1, &messageType, &messageId, &messageData);
			while(messageType != 2 || messageId != 0)
			{
				BDC_WaitForMessage(testSerialNo, 1, &messageType, &messageId, &messageData);
			}

			// set velocity if desired
			if(velocity > 0)
			{
				int currentVelocity, currentAcceleration;
				BDC_GetVelParams(testSerialNo, 1, &currentAcceleration, &currentVelocity);
				BDC_SetVelParams(testSerialNo, 1, currentAcceleration, velocity);
			}

			// move to position (channel 1)
			BDC_ClearMessageQueue(testSerialNo, 1);
			BDC_MoveToPosition(testSerialNo, 1, position);
			printf("Device %s moving\r\n", testSerialNo);

			// wait for completion
			BDC_WaitForMessage(testSerialNo, 1, &messageType, &messageId, &messageData);
			while(messageType != 2 || messageId != 1)
			{
				BDC_WaitForMessage(testSerialNo, 1, &messageType, &messageId, &messageData);
			}

			// get actual poaition
			int pos = BDC_GetPosition(testSerialNo, 1);
			printf("Device %s moved to %d\r\n", testSerialNo, pos);

			// stop polling
			BDC_StopPolling(testSerialNo, 1);
			// close device
			BDC_Close(testSerialNo);
	    }
    }
	
	// Uncomment this line if you are using simulations
	//TLI_UnitializeSimulations;
	char c = _getch();
	return 0;
}
