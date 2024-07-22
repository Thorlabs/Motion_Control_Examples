/*
PDXC2 Simple Example
Date of Creation(YYYY-MM-DD): 2024-01-26
Date of Last Modification on Github: 2024-01-26
C++ Version Used: ISO C++ 14
Kinesis Version Tested: 1.14.45
*/

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

// Include device-specific header file
#include "Thorlabs.MotionControl.Benchtop.Piezo.PDXC2.h"

int __cdecl wmain(int argc, wchar_t* argv[])
{
	// Uncomment this line (and TLI_UnitializeSimulations at the bottom of the page)
	// If you are using a simulated device
	//TLI_InitializeSimulations();

	// Change this line to reflect your device's serial number
	int serialNo = 112000001;

	// Set the target position of the device (device unit)
	int position = 10000;
	
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
		TLI_GetDeviceListByTypeExt(serialNos, 100, 112);

		// Search serial numbers for given serial number
		if (strstr(serialNos, testSerialNo)) {
			printf("Device %s found\r\n", testSerialNo);
		}
		else {
			printf("Device %s Not Found\r\n", testSerialNo);
			return -1;
		}
		
		// open device
		if (PDXC2_Open(testSerialNo) == 0)
		{
			// start the device polling at 200ms intervals
			PDXC2_StartPolling(testSerialNo, 200);

			// NOTE The following uses Sleep functions to simulate timing
			// In reality, the program should read the status to check that commands have been completed
			Sleep(1000);

			// Set open loop mode
			PDXC2_SetPositionControlMode(testSerialNo, PZ_ControlModeTypes::PZ_OpenLoop);

			// Set the target position
			PDXC2_OpenLoopMoveParameters openLoopParams;
			openLoopParams.StepSize = position;
			PDXC2_SetOpenLoopMoveParams(testSerialNo, &openLoopParams);
			Sleep(1000);

			PDXC2_OpenLoopMoveParameters openLoopParamsGet;
			PDXC2_GetOpenLoopMoveParams(testSerialNo, &openLoopParamsGet);

			if (openLoopParamsGet.StepSize != position)
			{
				printf("fail to set the position");
			}
			else
			{
				// Continuous Move
				PDXC2_MoveStart(testSerialNo);
				printf("Start moving.\r\n");

				// Judge if the stage reaches the target postion
				int newPos = 0;
				PDXC2_GetPosition(testSerialNo, &newPos);
				while (position != newPos)
				{
					PDXC2_GetPosition(testSerialNo, &newPos);
				}

				// Stage moved to the target position. Display the current position
				printf("Device Moved to %d\r\n", newPos);
			}

			// stop polling
			PDXC2_StopPolling(testSerialNo);
			// close device
			PDXC2_Close(testSerialNo);
			printf("Program Finished.");
		}
	}

	// Uncomment this line if you are using simulations
	//TLI_UninitializeSimulations;
	char c = _getch();
	return 0;
}
