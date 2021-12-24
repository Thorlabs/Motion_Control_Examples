// Example_TLS001.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <stdlib.h>
#include <conio.h>

#if defined TestCode
	#include "..\..\..\Instruments\Thorlabs.TCube.LaserSource\Thorlabs.TCube.LaserSource\Thorlabs.MotionControl.TCube.LaserSource.h"
#else
	#include "Thorlabs.MotionControl.TCube.LaserSource.h"
#endif

/// <summary> Main entry-point for this application. </summary>
/// <param name="argc"> The argc. </param>
/// <param name="argv"> The argv. </param>
/// <returns> . </returns>
int __cdecl wmain(int argc, wchar_t* argv[])
{
	if(argc < 1)
	{
		printf("Usage = Example_TLS001 [serial_no] [power: optional (0 - 32767)]\r\n");
		char c = _getch();
		return 1;
	}

	int serialNo = 86837825;
	if(argc > 1)
	{
		serialNo = _wtoi(argv[1]);
	}

	// get parameters from command line
	WORD power = 0;
	if(argc > 2)
	{
		power = _wtoi(argv[2]);
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
		TLI_GetDeviceListByTypeExt(serialNos, 100, 86);

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
		if(LS_Open(testSerialNo) == 0)
		{
			// start the device polling at 200ms intervals
			LS_StartPolling(testSerialNo, 200);

			// NOTE The following uses Sleep functions to simulate timing
			// In reality, the program should read the status to check that commands have been completed
			Sleep(1000);

			LS_SetPower(testSerialNo, power);
			printf("Device %s setting power %d\r\n", testSerialNo, power);
			Sleep(1000);

			WORD readPower = LS_GetPowerReading(testSerialNo);
			WORD readCurrent = LS_GetCurrentReading(testSerialNo);
			printf("Device %s read power %d\r\n", testSerialNo, readPower);
			printf("Device %s read current %d\r\n", testSerialNo, readCurrent);

			Sleep(1000);

			// stop polling
			LS_StopPolling(testSerialNo);
			// close device
			LS_Close(testSerialNo);
	    }
    }

	char c = _getch();
	return 0;
}
