/*
TQD001 Simple Example
Date of Creation(YYYY-MM-DD): 2022-01-18
Date of Last Modification on Github: 2022-09-21
C++ Version Used: ISO C++ 14
Kinesis Version Tested: 1.14.40
*/

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

#include "Thorlabs.MotionControl.TCube.Quad.h"

int __cdecl wmain(int argc, wchar_t* argv[])
{
	// Uncomment this line (and TLI_UnitializeSimulations at the bottom of the page)
	// If you are using a simulated device
	//TLI_InitializeSimulations();

	// Change this line to reflect your device's serial number
	int serialNo = 89000001;

	// identify and access device
	char testSerialNo[16];
	sprintf_s(testSerialNo, "%d", serialNo);

	// Optionally set the X and Y positions of the device
	QD_Position demandPosition = {0,0};

	// Build list of connected device
    if (TLI_BuildDeviceList() == 0)
    {
		// get device list size 
        short n = TLI_GetDeviceListSize();
		// get BBD serial numbers
        char serialNos[100];
		TLI_GetDeviceListByTypeExt(serialNos, 100, 89);

		// Search serial numbers for given serial number
		if (strstr(serialNos, testSerialNo)) {
			printf("Device %s found", testSerialNo);
		}
		else {
			printf("Device %s Not Found", testSerialNo);
			return -1;
		}

		// open device
		if(QD_Open(testSerialNo) == 0)
		{
			// start the device polling at 200ms intervals
			QD_StartPolling(testSerialNo, 200);

			// NOTE The following uses Sleep functions to simulate timing
			// In reality, the program should read the status to check that commands have been completed
			Sleep(1000);

			printf("Device %s set open loop mode\r\n", testSerialNo);
			QD_SetOperatingMode(testSerialNo, QD_OperatingMode::QD_OpenLoop);
			Sleep(100);

			QD_SetPosition(testSerialNo, &demandPosition);
			printf("Device %s set demand position (%d, %d)\r\n", testSerialNo, demandPosition.x, demandPosition.y);
			Sleep(1000);

			QD_Readings readPosition = {0,0};
			QD_GetReading(testSerialNo, &readPosition);
			printf("Device %s readings:\r\n", testSerialNo);
			printf("\tdemanded position (%d, %d)\r\n", readPosition.demandedPos.x, readPosition.demandedPos.y);
			printf("\tposition difference (%d, %d)\r\n", readPosition.posDifference.x, readPosition.posDifference.y);
			printf("\tsum %d\r\n", readPosition.sum);

			Sleep(100);

			// stop polling
			QD_StopPolling(testSerialNo);
			// close device
			QD_Close(testSerialNo);
	    }
    }

	// Uncomment this line if you are using simulations
	//TLI_UnitializeSimulations;
	char c = _getch();
	return 0;
}
