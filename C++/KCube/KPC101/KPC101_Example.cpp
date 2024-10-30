/*
KPC101 Simple Example
Date of Creation(YYYY-MM-DD): 2024-10-30
Date of Last Modification on Github: 2024-10-30
C++ Version Used: ISO C++ 14
Kinesis Version Tested: 1.14.50
*/

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#include "Thorlabs.MotionControl.KCube.PiezoStrainGauge.h"


int __cdecl wmain(int argc, wchar_t* argv[])
{
	// Uncomment this line (and TLI_UnitializeSimulations at the bottom of the page)
	// If you are using a simulated device
	// TLI_InitializeSimulations();

	// Change this line to reflect your device's serial number
	int serialNo = 113000001;

	// Optionally adjust the voltage to move your device to a new position in open loop mode
	float voltage = 0; //unit: V

	// Optionally adjust the position to move your device to a new position in closed loop mode
	// CAUTION: Change the position only when a strain gauge reader is connected. 
	float position = 0; //unit: um

	// identify and access device
	char testSerialNo[16];
	sprintf_s(testSerialNo, "%d", serialNo);

	// Build list of connected device
	if (TLI_BuildDeviceList() == 0)
	{
		// get device list size 
		short n = TLI_GetDeviceListSize();
		// get KPC serial numbers
		char serialNos[100];
		TLI_GetDeviceListByTypeExt(serialNos, 100, 113);

		// Search serial numbers for given serial number
		if (strstr(serialNos, testSerialNo)) {
			printf("Device %s found\n", testSerialNo);
		}
		else {
			printf("Device %s Not Found\n", testSerialNo);
			return -1;
		}

		// open device
		if (KPC_Open(testSerialNo) == 0)
		{
			// start the device polling at 200ms intervals
			KPC_StartPolling(testSerialNo, 200);

			//Zero the voltage
			printf("Setting Zero Point\n");
			KPC_SetZero(testSerialNo);
			Sleep(5000);

			//Optionally set the deivce to Open Loop Mode and apply the target voltage to the piezo
			if (voltage != 0)
			{
				//Set the max output voltage to 75 V
				KPC_SetHardwareMaxOutputVoltage(testSerialNo, 75);
				KPC_SetMaxOutputVoltage(testSerialNo,75);

				//Get the max output voltage
				short maxVoltage = KPC_GetMaxOutputVoltage(testSerialNo);

				if (voltage > 0 && voltage <= maxVoltage)
				{
					// Set open loop mode
					KPC_SetPositionControlMode(testSerialNo, PZ_ControlModeTypes::PZ_OpenLoop);

					//Convert the voltage to device Unit
					short voltageDeviceUnit = voltage / maxVoltage * 32767;

					// Set voltage
					printf("Going to voltage %.2f V\r\n", voltage);
					KPC_SetOutputVoltage(testSerialNo, voltageDeviceUnit);
					Sleep(5000);

					// get output voltage
					float voltageOutDeviceUnit = KPC_GetOutputVoltage(testSerialNo);
					printf("Moved to voltage %.2f V\r\n", voltageOutDeviceUnit / 32767 * maxVoltage);
					Sleep(1000);
				}
				else
				{
					printf("Voltage must be between 0 and %hd V\n", maxVoltage);
				}

			}

			//Optionally set the deivce to Closed Loop Mode and move the deivce to a new position
			//CAUTION: set a non-zero position only when a strain gauge reader is connected. 
			if (position != 0)
			{
				WORD _cdecl maxTravel = KPC_GetMaximumTravel(testSerialNo) * 0.1;

				if (position > 0 && position <= maxTravel)
				{
					// Set close loop mode
					KPC_SetPositionControlMode(testSerialNo, PZ_ControlModeTypes::PZ_CloseLoop);

					//Convert the position to device Unit
					WORD positionDeviceUnit = position / maxTravel * 32767;

					// Set position
					printf("Going to position %.3f um\r\n", position);
					KPC_SetPosition(testSerialNo, positionDeviceUnit);
					Sleep(5000);

					// get position
					float positionOutDeviceUnit = KPC_GetPosition(testSerialNo);
					printf("Moved to position %.3f um\r\n", positionOutDeviceUnit / 32767 * maxTravel);
					Sleep(1000);
				}
				else
				{
					printf("Position must be between 0 and %d um\n", maxTravel);
				}

			}
			// stop polling
			KPC_StopPolling(testSerialNo);
			// close device
			KPC_Close(testSerialNo);
			printf("Program finished.\n");
		}
	}

	// Uncomment this line if you are using simulations
	// TLI_UninitializeSimulations;
	char c = _getch();
	return 0;
}
