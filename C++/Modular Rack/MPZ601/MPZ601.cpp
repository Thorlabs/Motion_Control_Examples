// Example_MPZ601.cpp : Defines the entry point for the console application.
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

		// output list of matching devices
		{
			bool matched = false;
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
				if (strncmp(testSerialNo, serialNo, 8) == 0)
				{
					printf("requested device %s found\r\n", serialNo);
					matched = true;
				}
			}

			if (!matched)
			{
				printf("Piezo %s not found\r\n", testSerialNo);
				char c = _getch();
				return 1;
			}
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
