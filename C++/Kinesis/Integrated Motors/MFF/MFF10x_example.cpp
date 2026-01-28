// 
// C++ example for Thorlabs MFF10X Filter Flippers 
//2023 - 10 - 02
//2023 - 10 - 02
//C++20
//Kinesis version 1.14.41
//=======================
//This example goes over connecting to the device, moveing between states and disconnecting from the Console
// 

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

// Include device-specific header file.
#include "ThorLabs.MotionControl.FilterFlipper.h"

int main()
{
	// Uncomment this line (and TLI_UnitializeSimulations at the bottom of the page)
	// If you are using a simulated device
	//TLI_InitializeSimulations();

	// Change this line to reflect your device's serial number
	int serialNo = 37007009;


	char testSerialNo[16];
	sprintf_s(testSerialNo, "%d", serialNo);

	// Build list of connected device
	if (TLI_BuildDeviceList() == 0)
	{
		// get device list size 
		short n = TLI_GetDeviceListSize();
		// get MFF serial numbers
		char serialNos[100];
		TLI_GetDeviceListByTypeExt(serialNos, 100, 37);

		// output list of matching devices
		{
			char* searchContext = nullptr;
			char* p = strtok_s(serialNos, ",", &searchContext);

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

		// Open device.
		if (FF_Open(testSerialNo) == 0)
		{
			// Start the device polling.
			FF_StartPolling(testSerialNo, 200);

			Sleep(300);

			FF_ClearMessageQueue(testSerialNo);

			FF_Home(testSerialNo);
				printf("Device %s homing\r\n", testSerialNo);

			FF_MoveToPosition(testSerialNo, FF_Positions::Position2);

			Sleep(2000);

			FF_MoveToPosition(testSerialNo, FF_Positions::Position1);

			Sleep(2000);

			
			printf("Device %s current position is %d\r\n", testSerialNo, FF_GetPosition(testSerialNo));

			// stop polling
			FF_StopPolling(testSerialNo);
			// close device
			FF_Close(testSerialNo);
			// TLI_UninitializeSimulations();
		}
	}
}



