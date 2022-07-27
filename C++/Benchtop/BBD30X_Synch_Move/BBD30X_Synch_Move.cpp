// BBD30X_Synch_Move.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <stdio.h>
#include <conio.h>

#include "Thorlabs.MotionControl.Benchtop.BrushlessMotor.h"

int main()
{
	// Uncomment this line (and TLI_UnitializeSimulations at the bottom of the page)
	// If you are using a simulated device
	TLI_InitializeSimulations();

	// Change this line to reflect your device's serial number
	int serialNo = 103000001;

	// identify and access device
	char testSerialNo[16];
	sprintf_s(testSerialNo, "%d", serialNo);

	if (TLI_BuildDeviceList() == 0) {
		// get device list size 
		short n = TLI_GetDeviceListSize(); // not used here, but useful

		if (BMC_Open(testSerialNo) == 0) {
			// device successfully opened, no error
			// Begin polling on two channels and enable

			BMC_StartPolling(testSerialNo, 1, 250);
			BMC_StartPolling(testSerialNo, 2, 250);
			Sleep(500); // Allow time for devices to respond

			BMC_EnableChannel(testSerialNo, 1);
			BMC_EnableChannel(testSerialNo, 2);
			Sleep(500);

			BMC_ClearMessageQueue(testSerialNo, 1);

			// Home both channels
			WORD messageType; // aka unsigned short
			WORD messageId;
			DWORD messageData; // aka unsigned long

			printf("Channel 1 Homing");
			BMC_Home(testSerialNo, 1);
			// Wait for "Homing Complete" Message on channel 1
			BMC_WaitForMessage(testSerialNo, 1, &messageType, &messageId, &messageData);
			while (messageType != 2 || messageId != 0)
			{
				BMC_WaitForMessage(testSerialNo, 1, &messageType, &messageId, &messageData);
			}

			printf("Channel 2 Homing");
			BMC_Home(testSerialNo, 1);
			BMC_WaitForMessage(testSerialNo, 2, &messageType, &messageId, &messageData);
			while (messageType != 2 || messageId != 0)
			{
				BMC_WaitForMessage(testSerialNo, 2, &messageType, &messageId, &messageData);
			}

			printf("Both Channels Homed");
		}

	}
	// We'll not be setting velocity parameters or moving

	// Uncomment this line if you are using simulations
	TLI_UninitializeSimulations();
	char c = _getch();
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
