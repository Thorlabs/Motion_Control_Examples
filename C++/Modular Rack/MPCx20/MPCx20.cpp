#include <stdlib.h>
#include <conio.h>
#include <iostream>

#include "Thorlabs.MotionControl.Polarizer.h"



int __cdecl wmain(int argc, wchar_t* argv[])
{
	
	int serialNo = 38837825;


	// identify and access device
	char testSerialNo[16];
	sprintf_s(testSerialNo, "%d", serialNo);

	// Build list of connected device
	if (TLI_BuildDeviceList() == 0)
	{
		// get device list size 
		short n = TLI_GetDeviceListSize();
		// get MPCx20 serial numbers
		char serialNos[100];
		TLI_GetDeviceListByTypeExt(serialNos, 100, 38);

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
		if (MPC_Open(testSerialNo) == 0)
		{
			// start the device polling at 200ms intervals
			MPC_StartPolling(testSerialNo, 200);

			// NOTE The following uses Sleep functions to simulate timing
			// In reality, the program should read the status to check that commands have been completed
			Sleep(1000);

			// get conversion factor between degrees and steps
			double stepsPerDegree = MPC_GetStepsPerDegree(testSerialNo);

			for (POL_Paddles paddle = POL_Paddles::paddle1; paddle <= POL_Paddles::paddle3; paddle = static_cast<POL_Paddles>(static_cast<int>(paddle) + 1))
			{
				MPC_Home(testSerialNo, paddle);
				Sleep(1000);

				int position = (int)MPC_GetPosition(testSerialNo, paddle);
				printf("Device %s (channel %d) current position is %d\r\n", testSerialNo, (int)paddle, position);

				// move to next position
				MPC_MoveToPosition(testSerialNo, paddle, 30.0);
				printf("Device %s (channel %d) moving\r\n", testSerialNo, paddle);
				Sleep(1000);

				position = (int)MPC_GetPosition(testSerialNo, paddle);
				printf("Device %s (channel %d) current position is %d\r\n", testSerialNo, (int)paddle, position);
			}

			// stop polling
			MPC_StopPolling(testSerialNo);
			// close device
			MPC_Close(testSerialNo);
		}
	}

	char c = _getch();
	return 0;
}
