/*
PDXC2 Simple Example
Date of Creation(YYYY-MM-DD): 2024-01-26
Date of Last Modification on Github: 2025-11-17
C++ Version Used: ISO C++ 14
Kinesis Version Tested: 1.14.56
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
	// TLI_InitializeSimulations();

	// Change this line to reflect your device's serial number
	int serialNo = 112000001;
	
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
			Sleep(500);

			//Enalbe device
			PDXC2_Enable(testSerialNo);

			//Optionally set the deivce to Open Loop Mode and move the stage to target position (position is set in "steps")
			int openLoopPosition = 0;
			if (openLoopPosition != 0)
			{
				// Set open loop mode
				PDXC2_SetPositionControlMode(testSerialNo, PZ_ControlModeTypes::PZ_OpenLoop);

				// Set the target position
				PDXC2_OpenLoopMoveParameters openLoopParams;
				openLoopParams.StepSize = openLoopPosition;
				PDXC2_SetOpenLoopMoveParams(testSerialNo, &openLoopParams);
				Sleep(200);

				// Continuous Move
				PDXC2_MoveStart(testSerialNo);
				printf("Start moving.\r\n");

				// wait for completion
				int newPos = 0;
				PDXC2_GetPosition(testSerialNo, &newPos);
				while (openLoopPosition != newPos)
				{
					PDXC2_GetPosition(testSerialNo, &newPos);
					Sleep(200);
				}

				// Stage moved to the target position. Display the current position
				printf("Device Moved to %d\r\n", newPos);
			}

			//Optionally set the deivce to Closed Loop Mode and move the stage to target position
            //Close loop mode is only valid for PDX series stages with encoder
			//For linear stages, the position is in nm
			//For rotational stages, 360 degrees corresponds to 14400000 encoder counts
			int closeLoopPosition = 0;
			if (closeLoopPosition != 0)
			{
				// Set closed loop mode
				PDXC2_SetPositionControlMode(testSerialNo, PZ_ControlModeTypes::PZ_CloseLoop);

				// Performance optimize
				PDXC2_PulseParamsAcquireStart(testSerialNo);
				Sleep(500);
				printf("Optimizing performance, please wait...\r\n");
				bool pulseParamAcquired = false;
				// When pulseParamAcquired is true, it indicates the optimization has finished
				while (pulseParamAcquired == false)
				{
					pulseParamAcquired = (PDXC2_GetStatusBits(testSerialNo) & 0x00400000) != 0;
					Sleep(500);
				}

				// home the device
				printf("Home the device.\r\n");
				PDXC2_Home(testSerialNo);
				// wait for completion
				int posCheckCnt = 0, newPos = 0;
				for (int i = 0; i < 200; i++)
				{
					PDXC2_GetPosition(testSerialNo, &newPos);
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
					Sleep(200);
				}

				// Set the target position
				PDXC2_SetClosedLoopTarget(testSerialNo, closeLoopPosition);

				// Get and Set the velocity and acceleration
				// For linear stages, the unit is in nm/s and nm/s^2
				// For rotational stages, 360 degrees corresponds to 14400000 EnCnt. For example, 30 degrees/s = 1200000 EnCnt/s
				PDXC2_ClosedLoopParameters closedLoopParams;
				PDXC2_GetClosedLoopParams(testSerialNo, &closedLoopParams);
				closedLoopParams.RefSpeed = 1200000; 
				closedLoopParams.Acceleration = 1200000; 
				PDXC2_SetClosedLoopParams(testSerialNo, &closedLoopParams);

				// Move the stage to the target position
				PDXC2_MoveStart(testSerialNo);
				printf("Start moving.\r\n");

				// wait for completion
				posCheckCnt = 0;
				newPos = 0;
				for (int i = 0; i < 200; i++)
				{
					PDXC2_GetPosition(testSerialNo, &newPos);
					if (abs(newPos - closeLoopPosition) < 6000)
					{
						if (posCheckCnt > 3)
							break;
						else
						{
							Sleep(200);
							posCheckCnt++;
						}
					}
					Sleep(200);
				}

				// Stage moved to the target position. Display the current position
				printf("Device moved to %d.\r\n", newPos);
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
