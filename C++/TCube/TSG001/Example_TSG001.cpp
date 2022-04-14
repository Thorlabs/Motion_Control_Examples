// Example_TSG001.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

// Include device-specific header file
#include "Thorlabs.MotionControl.TCube.StrainGauge.h"

int __cdecl wmain(int argc, wchar_t* argv[])
{
	// Uncomment this line (and TLI_UnitializeSimulations at the bottom of the page)
	// If you are using a simulated device
	//TLI_InitializeSimulations();

	// Change this line to reflect your device's serial number
	int serialNo = 84000001;

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
		TLI_GetDeviceListByTypeExt(serialNos, 100, 84);

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
		if (SG_Open(testSerialNo) == 0)
		{
			// start the device polling at 200ms intervals
			SG_StartPolling(testSerialNo, 200);

			// NOTE The following uses Sleep functions to simulate timing
			// In reality, the program should read the status to check that commands have been completed
			Sleep(1000);

			// Set reference
			SG_SetZero(testSerialNo);
			Sleep(1000);

			bool overrange;
			SG_SetDisplayMode(testSerialNo, TSG_Display_Modes::TSG_Position);
			int voltage = SG_GetReadingExt(testSerialNo, false, &overrange);
			printf("Device %s position = %d\r\n", testSerialNo, voltage);
			Sleep(1000);

			SG_SetDisplayMode(testSerialNo, TSG_Display_Modes::TSG_Voltage);
			int pos = SG_GetReadingExt(testSerialNo, false, &overrange);
			printf("Device %s voltage = %d\r\n", testSerialNo, pos);
			Sleep(1000);

			SG_SetDisplayMode(testSerialNo, TSG_Display_Modes::TSG_Force);
			int force = SG_GetReadingExt(testSerialNo, false, &overrange);
			printf("Device %s Force = %d\r\n", testSerialNo, force);
			Sleep(1000);

			// stop polling
			SG_StopPolling(testSerialNo);
			// close device
			SG_Close(testSerialNo);
		}
	}

	// Uncomment this line if you are using simulations
	//TLI_UnitializeSimulations;
	char c = _getch();
	return 0;
}
