// Example_KPZ101.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

#include "Thorlabs.MotionControl.KCube.Piezo.h"


int __cdecl wmain(int argc, wchar_t* argv[])
{

	// Uncomment this line (and TLI_UnitializeSimulations at the bottom of the page)
	// If you are using a simulated device
	//TLI_InitializeSimulations();
	
	// Change this line to reflect your device's serial number
	int serialNo = 81000001;

	// Optionally adjust this value to move your device to a new position (in device units)
	int position = 0;

	// identify and access device
	char testSerialNo[16];
	sprintf_s(testSerialNo, "%d", serialNo);

	// Build list of connected device
	if (TLI_BuildDeviceList() == 0)
	{
		// get device list size 
		short n = TLI_GetDeviceListSize();
		// get KPZ serial numbers
		char serialNos[100];
		TLI_GetDeviceListByTypeExt(serialNos, 100, 81);

		// Search serial numbers for given serial number
		if (strstr(serialNos, testSerialNo)) {
			printf("Device %s found", testSerialNo);
		}
		else {
			printf("Device %s Not Found", testSerialNo);
			return -1;
		}

		// open device
		if (PCC_Open(testSerialNo) == 0)
		{
			// start the device polling at 200ms intervals
			PCC_StartPolling(testSerialNo, 200);

			// NOTE The following uses Sleep functions to simulate timing
			// In reality, the program should read the status to check that commands have been completed
			Sleep(1000);
			// Set open loop mode
			PCC_SetPositionControlMode(testSerialNo, PZ_ControlModeTypes::PZ_OpenLoop);
			// Set position
			printf("Set %s position\r\n", testSerialNo);
			PCC_SetPosition(testSerialNo, position);
			Sleep(1000);
			
			// get output voltage
			int voltage = PCC_GetOutputVoltage(testSerialNo);
			printf("Device %s voltage = %d\r\n", testSerialNo, voltage);
			Sleep(1000);

			// stop polling
			PCC_StopPolling(testSerialNo);
			// close device
			PCC_Close(testSerialNo);
		}
	}

	// Uncomment this line if you are using simulations
	//TLI_UnitializeSimulations;
	char c = _getch();
	return 0;
}
