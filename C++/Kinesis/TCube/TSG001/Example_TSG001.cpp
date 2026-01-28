/*
TSG001 Simple Example
Date of Creation(YYYY-MM-DD): 2022-01-18
Date of Last Modification on Github: 2022-09-21
C++ Version Used: ISO C++ 14
Kinesis Version Tested: 1.14.40
*/

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

		// Search serial numbers for given serial number
		if (strstr(serialNos, testSerialNo)) {
			printf("Device %s found", testSerialNo);
		}
		else {
			printf("Device %s Not Found", testSerialNo);
			return -1;
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
