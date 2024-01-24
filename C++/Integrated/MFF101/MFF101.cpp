/*
MFF101 Simple Example
Date of Creation(YYYY-MM-DD): 2022-05-16
Date of Last Modification on Github: 2022-09-21
C++ Version Used: ISO C++ 14
Kinesis Version Tested: 1.14.40
*/

#include <stdlib.h>
#include <conio.h>
#include <stdio.h>

#include "Thorlabs.MotionControl.FilterFlipper.h"


int __cdecl wmain(int argc, wchar_t* argv[])
{

	int serialNo = 37837825;


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

		// Search serial numbers for given serial number
		if (strstr(serialNos, testSerialNo)) {
			printf("Device %s found", testSerialNo);
		}
		else {
			printf("Device %s Not Found", testSerialNo);
			return -1;
		}

		// open device
		if (FF_Open(testSerialNo) == 0)
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
