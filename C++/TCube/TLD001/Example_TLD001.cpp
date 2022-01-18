// Example_TLD001.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <stdlib.h>
#include <conio.h>

#if defined TestCode
	#include "..\..\..\Instruments\Thorlabs.TCube.LaserDiode\Thorlabs.TCube.LaserDiode\Thorlabs.MotionControl.TCube.LaserDiode.h"
#else
	#include "Thorlabs.MotionControl.TCube.LaserDiode.h"
#endif

/// <summary> Main entry-point for this application. </summary>
/// <param name="argc"> The argc. </param>
/// <param name="argv"> The argv. </param>
/// <returns> . </returns>
int __cdecl wmain(int argc, wchar_t* argv[])
{
	if(argc < 1)
	{
		printf("Usage = Example_TLD001 [serial_no] [power: optional (0 - 32767)]\r\n");
		char c = _getch();
		return 1;
	}

	int serialNo = 86837825;
	if(argc > 1)
	{
		serialNo = _wtoi(argv[1]);
	}

	// get parameters from command line
	WORD setPoint = 100;
	if(argc > 2)
	{
		setPoint = _wtoi(argv[2]);
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
		if(LD_Open(testSerialNo) == 0)
		{
			// start the device polling at 200ms intervals
			LD_StartPolling(testSerialNo, 200);

			// NOTE The following uses Sleep functions to simulate timing
			// In reality, the program should read the status to check that commands have been completed
			Sleep(1000);

			LD_SetOpenLoopMode(testSerialNo);
			LD_EnableOutput(testSerialNo);
			LD_SetLaserSetPoint(testSerialNo, setPoint);
			printf("Device %s set point %d\r\n", testSerialNo, setPoint);
			Sleep(1000);

			WORD readCurrent = LD_GetLaserDiodeCurrentReading(testSerialNo);
			float waFactor = LD_GetWACalibFactor(testSerialNo);
			printf("Device %s read current %d\r\n", testSerialNo, readCurrent);
			printf("Device %s read power %f\r\n", testSerialNo, (float)readCurrent * waFactor);

			Sleep(1000);

			// stop polling
			LD_StopPolling(testSerialNo);
			// close device
			LD_Close(testSerialNo);
	    }
    }

	char c = _getch();
	return 0;
}
