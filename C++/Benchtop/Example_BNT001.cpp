// Example_BNT001.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <stdlib.h>
#include <conio.h>

#if defined TestCode
	#include "..\..\..\Instruments\Thorlabs.Benchtop.NanoTrak\Thorlabs.Benchtop.NanoTrak\Thorlabs.MotionControl.Benchtop.NanoTrak.h"
#else
	#include "Thorlabs.MotionControl.Benchtop.NanoTrak.h"
#endif

/// <summary> Main entry-point for this application. </summary>
/// <param name="argc"> The argc. </param>
/// <param name="argv"> The argv. </param>
/// <returns> . </returns>
int __cdecl wmain(int argc, wchar_t* argv[])
{
	if(argc < 1)
	{
		printf("Usage = Example_BNT001 [serial_no] [h position: optional (0 - 65535)] [v position: optional (0 - 65535)]\r\n");
		char c = _getch();
		return 1;
	}

	int serialNo = 22837825;
	if(argc > 1)
	{
		serialNo = _wtoi(argv[1]);
	}

	// get parameters from command line
	NT_HVComponent position;
	position.horizontalComponent = 0x8000;
	position.verticalComponent = 0x8000;
	if(argc > 3)
	{
		position.horizontalComponent = _wtoi(argv[2]);
		position.verticalComponent = _wtoi(argv[3]);
	}

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

	char c = _getch();
	return 0;
}
