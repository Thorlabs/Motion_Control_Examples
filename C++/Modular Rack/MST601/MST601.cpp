// Example_MST601.cpp : Defines the entry point for the console application.
#include <stdlib.h>
#include <conio.h>
#include <stdio.h>

#include "Thorlabs.MotionControl.ModularRack.StepperMotor.h"


int __cdecl wmain(int argc, wchar_t* argv[])
{
	int serialNo = 50837825;
	int channelNo = 1;

	int position = 0;

	int velocity = 0;

	// identify and access device
	char testSerialNo[16];
	sprintf_s(testSerialNo, "%d", serialNo);

	// Build list of connected device
	if (TLI_BuildDeviceList() == 0)
	{
		// get device list size 
		short n = TLI_GetDeviceListSize();
		// get MST serial numbers
		char serialNos[100];
		// params define buffer size and module type 50 = Stepper Module
		TLI_GetDeviceListByTypeExt(serialNos, 100, 50);

		// Search serial numbers for given serial number
		if (strstr(serialNos, testSerialNo)) {
			printf("Device %s found", testSerialNo);
		}
		else {
			printf("Device %s Not Found", testSerialNo);
			return -1;
		}

		// open device
		if (MMR_Open(testSerialNo) == 0)
		{
			// start the device polling at 200ms intervals
			SBC_StartPolling(testSerialNo, channelNo, 200);

			Sleep(3000);
			// Home device
			MMR_ClearMessageQueue(testSerialNo, channelNo);
			SBC_Home(testSerialNo, channelNo);
			printf("Device %s homing\r\n", testSerialNo);

			// wait for completion
			WORD messageType;
			WORD messageId;
			DWORD messageData;
			MMR_WaitForMessage(testSerialNo, channelNo, &messageType, &messageId, &messageData);
			while (messageType != 2 || messageId != 0)
			{
				MMR_WaitForMessage(testSerialNo, channelNo, &messageType, &messageId, &messageData);
			}

			// set velocity if desired
			if (velocity > 0)
			{
				int currentVelocity, currentAcceleration;
				SBC_GetVelParams(testSerialNo, channelNo, &currentAcceleration, &currentVelocity);
				SBC_SetVelParams(testSerialNo, channelNo, currentAcceleration, velocity);
			}

			// move to position (channel 1)
			MMR_ClearMessageQueue(testSerialNo, channelNo);
			SBC_MoveToPosition(testSerialNo, channelNo, position);
			printf("Device %s moving\r\n", testSerialNo);

			// wait for completion
			MMR_WaitForMessage(testSerialNo, channelNo, &messageType, &messageId, &messageData);
			while (messageType != 2 || messageId != 1)
			{
				MMR_WaitForMessage(testSerialNo, channelNo, &messageType, &messageId, &messageData);
			}

			// get actual poaition
			int pos = SBC_GetPosition(testSerialNo, channelNo);
			printf("Device %s moved to %d\r\n", testSerialNo, pos);

			// stop polling
			SBC_StopPolling(testSerialNo, channelNo);
			// close device
			MMR_Close(testSerialNo);
		}
	}

	char c = _getch();
	return 0;
}
