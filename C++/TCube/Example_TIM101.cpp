// Example_TIM101.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <stdlib.h>
#include <conio.h>

#if defined TestCode
	#include "..\..\..\Instruments\Thorlabs.TCube.InertialMotor\Thorlabs.TCube.InertialMotor\Thorlabs.MotionControl.TCube.InertialMotor.h"
#else
	#include "Thorlabs.MotionControl.TCube.InertialMotor.h"
#endif

/// <summary> Main entry-point for this application. </summary>
/// <param name="argc"> The argc. </param>
/// <param name="argv"> The argv. </param>
/// <returns> . </returns>
int __cdecl wmain(int argc, wchar_t* argv[])
{
	if(argc < 1)
	{
		printf("Usage = Example_TIM101 [serial_no]\r\n");
		char c = _getch();
		return 1;
	}

	int serialNo = 85837825;
	if(argc > 1)
	{
		serialNo = _wtoi(argv[1]);
	}

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
		TLI_GetDeviceListByTypeExt(serialNos, 100, 85);

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

	char c = _getch();
	return 0;
}
