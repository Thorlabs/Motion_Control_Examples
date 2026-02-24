/*
UDXC Simple Example
Date of Creation(YYYY-MM-DD): 2025-10-27
Date of Last Modification on Github: 2025-10-27
C++ Version Used: ISO C++ 14
Kinesis Version Tested: 1.14.56
*/

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

// Include device-specific header file
#include "Thorlabs.MotionControl.Benchtop.Piezo.UDXC.h"


int __cdecl wmain(int argc, wchar_t* argv[])
{
	// Uncomment this line (and TLI_UnitializeSimulations at the bottom of the page)
	// If you are using a simulated device
	// TLI_InitializeSimulations();

	// Change this line to reflect your device's serial number
	int serialNo = 122000001;

	// Set the target position of the device (unit: nm)
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
		TLI_GetDeviceListByTypeExt(serialNos, 100, 122);

		// Search serial numbers for given serial number
		if (strstr(serialNos, testSerialNo)) 
		{
			printf("Device %s found.\r\n", testSerialNo);
		}
		else 
		{
			printf("Device %s not found.\r\n", testSerialNo);
			return -1;
		}
		
		// open device
		if (UDXC_Open(testSerialNo) == 0)
		{
			// start the device polling at 200ms intervals
			UDXC_StartPolling(testSerialNo, 200);
			Sleep(500);

			// enable device
			UDXC_Enable(testSerialNo);
			Sleep(500);

			// performance optimize
			UDXC_PulseParamsAcquireStart(testSerialNo);
			Sleep(500);
			printf("Optimizing performance, please wait...\r\n");
			bool pulseParamAcquired = false;
			// When pulseParamAcquired is true, it indicates the optimization has finished
			while (pulseParamAcquired == false)
			{
				pulseParamAcquired = (UDXC_GetStatusBits(testSerialNo) & 0x00400000) != 0;
				Sleep(500);
			}

			// home the device
			printf("Home the device.\r\n");
			UDXC_Home(testSerialNo);
			// wait for completion
			int posCheckCnt = 0, newPos = 0;
			for (int i = 0; i < 100; i++)
			{
				UDXC_GetPosition(testSerialNo,&newPos);

				if (abs(newPos - 0) < 6000)
				{
					if (posCheckCnt > 3) 
						break;
					else
					{
						Sleep(200);
						posCheckCnt++;
					}
				}
				else 
					Sleep(200);
			}

			// Set the target position
			UDXC_SetClosedLoopTarget(testSerialNo, position);

			// Get and Set the velocity and acceleration
			UDXC_ClosedLoopParameters closedLoopParams;
			UDXC_GetClosedLoopParams(testSerialNo, &closedLoopParams);
			closedLoopParams.RefSpeed = 10000000; // velocity is set in nm/s
			closedLoopParams.Acceleration = 10000000; // acceleration is set in nm/s^2
			UDXC_SetClosedLoopParams(testSerialNo, &closedLoopParams);

			// Move the stage to the target position
			UDXC_MoveStart(testSerialNo);
			printf("Start moving.\r\n");
			// wait for completion
			posCheckCnt = 0;
			newPos = 0;
			for (int i = 0; i < 100; i++)
			{
				UDXC_GetPosition(testSerialNo, &newPos);
				if (abs(newPos - position) < 6000)
				{
					if (posCheckCnt > 3)
						break;
					else
					{
						Sleep(200);
						posCheckCnt++;
					}
				}
				else
					Sleep(200);
			}

			// Stage moved to the target position. Display the current position
			printf("Device moved to %d nm.\r\n", newPos);

			// stop polling
			UDXC_StopPolling(testSerialNo);
			// close device
			UDXC_Close(testSerialNo);
			printf("Program Finished.");
		}
	}

	// Uncomment this line if you are using simulations
	// TLI_UninitializeSimulations;
	char c = _getch();
	return 0;
}
