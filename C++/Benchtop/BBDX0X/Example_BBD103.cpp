// Example_BBD103.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

#include "Thorlabs.MotionControl.Benchtop.BrushlessMotor.h"

int __cdecl wmain(int argc, wchar_t* argv[])
{
	// Uncomment this line (and TLI_UnitializeSimulations at the bottom of the page)
	// If you are using a simulated device
	//TLI_InitializeSimulations();

	// Change this line to reflect your device's serial number
	int serialNo = 73000001;

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
		TLI_GetDeviceListByTypeExt(serialNos, 100, 73);

		// output list of matching devices
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
		if(BMC_Open(testSerialNo) == 0)
		{
			// start the device polling at 200ms intervals
			BMC_StartPolling(testSerialNo, 1, 200);

			// enable device so that it can move
			BMC_EnableChannel(testSerialNo, 1);

			Sleep(3000);
			// Home device
			BMC_ClearMessageQueue(testSerialNo, 1);
			BMC_Home(testSerialNo, 1);
			printf("Device %s homing\r\n", testSerialNo);

			// wait for completion
			WORD messageType;
			WORD messageId;
			DWORD messageData;
			BMC_WaitForMessage(testSerialNo, 1, &messageType, &messageId, &messageData);
			while(messageType != 2 || messageId != 0)
			{
				BMC_WaitForMessage(testSerialNo, 1, &messageType, &messageId, &messageData);
			}

			// set velocity if desired
			if(velocity > 0)
			{
				int currentVelocity, currentAcceleration;
				BMC_GetVelParams(testSerialNo, 1, &currentAcceleration, &currentVelocity);
				BMC_SetVelParams(testSerialNo, 1, currentAcceleration, velocity);
			}

			// move to position (channel 1)
			BMC_ClearMessageQueue(testSerialNo, 1);
			BMC_MoveToPosition(testSerialNo, 1, position);
			printf("Device %s moving\r\n", testSerialNo);

			// wait for completion
			BMC_WaitForMessage(testSerialNo, 1, &messageType, &messageId, &messageData);
			while(messageType != 2 || messageId != 1)
			{
				BMC_WaitForMessage(testSerialNo, 1, &messageType, &messageId, &messageData);
			}
			// get actual poaition
			int pos = BMC_GetPosition(testSerialNo, 1);
			printf("Device %s moved to %d\r\n", testSerialNo, pos);

			// stop polling
			BMC_StopPolling(testSerialNo, 1);
			// close device
			BMC_Close(testSerialNo);
	    }
    }

	// Uncomment this line if you are using simulations
	//TLI_UnitializeSimulations;
	char c = _getch();
	return 0;
}
