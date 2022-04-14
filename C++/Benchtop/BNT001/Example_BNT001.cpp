// Example_BNT001.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

#include "Thorlabs.MotionControl.Benchtop.NanoTrak.h"

int __cdecl wmain(int argc, wchar_t* argv[])
{
	// Uncomment this line (and TLI_UnitializeSimulations at the bottom of the page)
	// If you are using a simulated device
	//TLI_InitializeSimulations();

	// Change this line to reflect your device's serial number
	int serialNo = 22000001;

	// Set the horizontal and vertical components of the position (in device units)
	NT_HVComponent position;
	position.horizontalComponent = 0x8000;
	position.verticalComponent = 0x8000;

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
		TLI_GetDeviceListByTypeExt(serialNos, 100, 22);

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
		if(NT_Open(testSerialNo) == 0)
		{
			// start the device polling at 200ms intervals
			NT_StartPolling(testSerialNo, 200);

			// NOTE The following uses Sleep functions to simulate timing
			// In reality, the program should read the status to check that commands have been completed
			Sleep(1000);
			// Home device
			printf("Device %s homing\r\n", testSerialNo);
			NT_SetCircleHomePosition(testSerialNo, &position);
			NT_HomeCircle(testSerialNo);
			Sleep(1000);

			// move to position (channel 1)
			NT_HVComponent pos;
			NT_GetCirclePosition(testSerialNo, &pos);
			printf("Device %s position = (%d, %d)\r\n", testSerialNo, pos.horizontalComponent, pos.verticalComponent);
			Sleep(1000);

			// stop polling
			NT_StopPolling(testSerialNo);
			// close device
			NT_Close(testSerialNo);
	    }
    }

	// Uncomment this line if you are using simulations
	//TLI_UnitializeSimulations;
	char c = _getch();
	return 0;
}
