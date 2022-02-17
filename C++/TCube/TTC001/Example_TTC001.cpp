// Example_TTC001.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <stdlib.h>
#include <conio.h>

#if defined TestCode
	#include "..\..\..\Instruments\Thorlabs.TCube.TEC\Thorlabs.TCube.TEC\Thorlabs.MotionControl.TCube.TEC.h"
#else
	#include "Thorlabs.MotionControl.TCube.TEC.h"
#endif

/// <summary> Main entry-point for this application. </summary>
/// <param name="argc"> The argc. </param>
/// <param name="argv"> The argv. </param>
/// <returns> . </returns>
int __cdecl wmain(int argc, wchar_t* argv[])
{
	if(argc < 1)
	{
		printf("Usage = Example_TTC001 [serial_no] [temperature: optional (0 - 32767)]\r\n");
		char c = _getch();
		return 1;
	}

	int serialNo = 87837825;
	if(argc > 1)
	{
		serialNo = _wtoi(argv[1]);
	}

	// get parameters from command line
	int temperature = 2000;
	if(argc > 2)
	{
		temperature = _wtoi(argv[2]);
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
		TLI_GetDeviceListByTypeExt(serialNos, 100, 87);

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
		if(TC_Open(testSerialNo) == 0)
		{
			// start the device polling at 200ms intervals
			TC_StartPolling(testSerialNo, 200);

			// NOTE The following uses Sleep functions to simulate timing
			// In reality, the program should read the status to check that commands have been completed
			Sleep(1000);

			TC_SetTemperature(testSerialNo, temperature);
			printf("Device %s Set Temperature %d\r\n", testSerialNo, temperature);
			Sleep(1000);

			for(int i=0; i<20; i++)
			{
				short current = TC_GetCurrentReading(testSerialNo);
				printf("Device %s Current is %d\r\n", testSerialNo, current);

				short actTemp = TC_GetTemperatureReading(testSerialNo);
				printf("Device %s Actual Temperature is %d\r\n", testSerialNo, actTemp);
				Sleep(200);
			}
			Sleep(1000);

			// stop polling
			TC_StopPolling(testSerialNo);
			// close device
			TC_Close(testSerialNo);
	    }
    }

	char c = _getch();
	return 0;
}
