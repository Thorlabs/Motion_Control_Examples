// Example_TIM101.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

#include "Thorlabs.MotionControl.TCube.InertialMotor.h"

int __cdecl wmain(int argc, wchar_t* argv[])
{
	// Uncomment this line (and TLI_UnitializeSimulations at the bottom of the page)
	// If you are using a simulated device
	//TLI_InitializeSimulations();

	// Change this line to reflect your device's serial number
	int serialNo = 65000001;

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
		TLI_GetDeviceListByTypeExt(serialNos, 100, 65);

		// Search serial numbers for given serial number
		if (strstr(serialNos, testSerialNo)) {
			printf("Device %s found", testSerialNo);
		}
		else {
			printf("Device %s Not Found", testSerialNo);
			return -1;
		}

		// open device
		if(TIM_Open(testSerialNo) == 0)
		{
			// start the device polling at 200ms intervals
			TIM_StartPolling(testSerialNo, 200);

			Sleep(1000);

			// initalize current position to zero
			TIM_SetPosition(testSerialNo, TIM_Channels::Channel1, 0);
			Sleep(1000);

			// Move to 
			TIM_MoveAbsolute(testSerialNo, TIM_Channels::Channel1, 1000);
			Sleep(200);
			printf("Device %s moving to 1000\r\n", testSerialNo);
			Sleep(5000);
					
			int pos = TIM_GetCurrentPosition(testSerialNo, TIM_Channels::Channel1);
			printf("Device %s position is %d\r\n", testSerialNo, pos);

			// Move Jog 
			TIM_MoveJog(testSerialNo, TIM_Channels::Channel1, TIM_Direction::Forward);
			Sleep(200);
			printf("Device %s jogging\r\n", testSerialNo);
			Sleep(2000);
					
			pos = TIM_GetCurrentPosition(testSerialNo, TIM_Channels::Channel1);
			printf("Device %s position is %d\r\n", testSerialNo, pos);


			// stop polling
			TIM_StopPolling(testSerialNo);
			// close device
			TIM_Close(testSerialNo);
	    }
    }

	// Uncomment this line if you are using simulations
	//TLI_UnitializeSimulations;
	char c = _getch();
	return 0;
}
