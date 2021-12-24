// Example_MFF101.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <stdlib.h>
#include <conio.h>

#if defined TestCode
	#include "..\..\..\Instruments\Thorlabs.FilterFlipper\Thorlabs.FilterFlipper\Thorlabs.MotionControl.FilterFlipper.h"
#else
	#include "Thorlabs.MotionControl.FilterFlipper.h"
#endif

/// <summary> Main entry-point for this application. </summary>
/// <param name="argc"> The argc. </param>
/// <param name="argv"> The argv. </param>
/// <returns> . </returns>
int __cdecl wmain(int argc, wchar_t* argv[])
{
	if(argc < 1)
	{
		printf("Usage = Example_MFF101 [serial_no]\r\n");
		char c = _getch();
		return 1;
	}

	int serialNo = 37837825;
	if(argc > 1)
	{
		serialNo = _wtoi(argv[1]);
	}

	// identify and access device
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
		if(FF_Open(testSerialNo) == 0)
		{
			// start the device polling at 200ms intervals
			FF_StartPolling(testSerialNo, 200);

			// NOTE The following uses Sleep functions to simulate timing
			// In reality, the program should read the status to check that commands have been completed
			Sleep(1000);

			int position = FF_GetPosition(testSerialNo);
			printf("Device %s current position is %d\r\n", testSerialNo, position);

			// move to next position
			FF_MoveToPosition(testSerialNo, position == 1 ? FF_Positions::Position2 : FF_Positions::Position1);
			printf("Device %s moving\r\n", testSerialNo);
			Sleep(1000);

			position = FF_GetPosition(testSerialNo);
			printf("Device %s current position is %d\r\n", testSerialNo, position);

			// stop polling
			FF_StopPolling(testSerialNo);
			// close device
			FF_Close(testSerialNo);
	    }
    }

	char c = _getch();
	return 0;
}
