/*
MPZ601 Simple Example
Date of Creation(YYYY-MM-DD): 2022-05-16
Date of Last Modification on Github: 2022-09-21
C++ Version Used: ISO C++ 14
Kinesis Version Tested: 1.14.40
*/

#include <stdlib.h>
#include <conio.h>
#include <stdio.h>

#include "Thorlabs.MotionControl.ModularRack.Piezo.h"

int __cdecl wmain(int argc, wchar_t* argv[])
{

	int serialNo = 51837825;
	int channelNo = 1;
	

	int position;
	position = 0;
	
	// identify and access device
	char testSerialNo[16];
	sprintf_s(testSerialNo, "%d", serialNo);

	// Build list of connected device
	if (TLI_BuildDeviceList() == 0)
	{
		// get device list size 
		short n = TLI_GetDeviceListSize();
		// get MST serial numbers
		char serialNos[100];
		// params define buffer size and module type 51 = Piezo Module
		TLI_GetDeviceListByTypeExt(serialNos, 100, 51);

		// Search serial numbers for given serial number
		if (strstr(serialNos, testSerialNo)) {
			printf("Device %s found", testSerialNo);
		}
		else {
			printf("Device %s Not Found", testSerialNo);
			return -1;
		}

		// open device
		if (MMR_Open(testSerialNo) == 0)
		{
			// start the device polling at 200ms intervals
			PBC_StartPolling(testSerialNo, channelNo, 200);

			// NOTE The following uses Sleep functions to simulate timing
			// In reality, the program should read the status to check that commands have been completed
			Sleep(1000);
			// Set open loop mode
			PBC_SetPositionControlMode(testSerialNo, channelNo, PZ_ControlModeTypes::PZ_OpenLoop);
			// Set position
			printf("Set %s position\r\n", testSerialNo);
			PBC_SetOutputVoltage(testSerialNo, channelNo, position);
			Sleep(1000);

			// get output voltage
			int voltage = PBC_GetOutputVoltage(testSerialNo, channelNo);
			printf("Device %s voltage = %d\r\n", testSerialNo, voltage);
			Sleep(1000);

			// stop polling
			PBC_StopPolling(testSerialNo, channelNo);
			// close device
			MMR_Close(testSerialNo);
		}
	}

	char c = _getch();
	return 0;
}
