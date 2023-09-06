// This example uses the Kinesis C++ API to move and control Thorlabs integrated stepper motor, LTS, K10CR1, and MLJ stages. 
//


#include <string> 
#include <iostream>
#include <stdio.h>
#include <stdlib.h>

#include "Thorlabs.MotionControl.IntegratedStepperMotors.h"


void waitMove(char serialNo[], long timeout);
void waitHome(char serialNo[], long timeout);

int main()
{
	//Sets up simulations. Comment in if running on physical hardware. 
	TLI_InitializeSimulations();

	//Input serial number. Change for your specific device. 
	char serialNum[9] = "45000001";
	int errorReturn = -1;

	//Build Device List and open device.
	TLI_BuildDeviceList();
	TLI_DeviceInfo info;
	TLI_GetDeviceInfo(serialNum, &info);

	std::cout << info.description;
	TLI_BuildDeviceList();
	Sleep(1000);

	errorReturn = ISC_Open(serialNum);
	Sleep(1000);
	if (errorReturn == 0)
	{
		std::cout << "Device Connected...\n";
		//Settings are loaded based on Stage Name. The integrated stepper class holds LTS and K10CR1 Information.
		ISC_StartPolling(serialNum, 50);
		Sleep(1000);

		//Set up homing parameters. 
		MOT_HomingParameters homingParams;
		ISC_GetHomingParamsBlock(serialNum, &homingParams);
		homingParams.direction = MOT_TravelDirection::MOT_Reverse;
		ISC_SetHomingParamsBlock(serialNum, &homingParams);

		//Clear existing messages in the hardware buffer.
		ISC_ClearMessageQueue(serialNum);

		//Home the stage and wait for the return message before continuing.
		ISC_Home(serialNum);
		std::cout << "Homing...\n";
		waitHome(serialNum, 100000);
		std::cout << "Homed...\n";

		//Move the stage and wait for the return message before continuing.
		// Set number of microsteps, found in APT communications protocol. Should be changed to 136533 if using K10CR1
		int conversionRate = 409600;

		//Move the stage and wait for the return message before continuing.
		ISC_SetMoveAbsolutePosition(serialNum, conversionRate * 5);
		ISC_MoveAbsolute(serialNum); 
		std::cout << "Moving ...\n";
		waitMove(serialNum, 10000);
		std::cout << "Move Complete...\n";

		//Close the stage
		ISC_StopPolling(serialNum);
		ISC_Close(serialNum);
		std::cout << "Device Disconnected...\n";
	}

	//Closes simulations. Comment if running on physical hardware. 
	//TLI_UninitializeSimulations();

	return 0;
}

//Waits should only be used for Home commands. The home command has a different status return.
void waitHome(char serialNo[], long timeout)// Waits until a single axis is homed.
{
	WORD messageType;
	WORD messageId;
	DWORD messageData;
	ISC_WaitForMessage(serialNo, &messageType, &messageId, &messageData);
	while (messageType != 2 || messageId != 0)
	{
		ISC_WaitForMessage(serialNo, &messageType, &messageId, &messageData);

	}
}

void waitMove(char serialNo[], long timeout)// Waits until axis is stopped.
{
	WORD messageType;
	WORD messageId;
	DWORD messageData;
	ISC_WaitForMessage(serialNo, &messageType, &messageId, &messageData);
	while (messageType != 2 || messageId != 1)
	{
		ISC_WaitForMessage(serialNo, &messageType, &messageId, &messageData);
	}
}