// Example_TTC001.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

// Include device-specific header file
#include "Thorlabs.MotionControl.TCube.TEC.h"

int __cdecl wmain(int argc, wchar_t* argv[])
{
	// Uncomment this line (and TLI_UnitializeSimulations at the bottom of the page)
	// If you are using a simulated device
	//TLI_InitializeSimulations();

	// Change this line to reflect your device's serial number
	int serialNo = 87000001;

	// Optionally set temperature 
	// (range and units depend on sensor, see documentation for TC_SetTemperature())
	int temperature = 2000;

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
		TLI_GetDeviceListByTypeExt(serialNos, 100, 87);

		// Search serial numbers for given serial number
		if (strstr(serialNos, testSerialNo)) {
			printf("Device %s found", testSerialNo);
		}
		else {
			printf("Device %s Not Found", testSerialNo);
			return -1;
		}

		// open device
		if(TC_Open(testSerialNo) == 0)
		{
			// start the device polling at 200ms intervals
			TC_StartPolling(testSerialNo, 200);

			// NOTE The following uses Sleep functions to simulate timing
			// In reality, the program should read the status to check that commands have been completed
			Sleep(1000);

			TC_SetTemperature(testSerialNo, temperature);
			printf("Device %s Set Temperature %d\r\n", testSerialNo, temperature);
			Sleep(1000);

			for(int i=0; i<20; i++)
			{
				short current = TC_GetCurrentReading(testSerialNo);
				printf("Device %s Current is %d\r\n", testSerialNo, current);

				short actTemp = TC_GetTemperatureReading(testSerialNo);
				printf("Device %s Actual Temperature is %d\r\n", testSerialNo, actTemp);
				Sleep(200);
			}
			Sleep(1000);

			// stop polling
			TC_StopPolling(testSerialNo);
			// close device
			TC_Close(testSerialNo);
	    }
    }

	// Uncomment this line if you are using simulations
	//TLI_UnitializeSimulations;
	char c = _getch();
	return 0;
}
