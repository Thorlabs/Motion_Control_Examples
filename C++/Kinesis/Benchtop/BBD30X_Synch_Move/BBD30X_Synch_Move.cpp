//BBD30x Synchronous Move
//Date of Creation(YYYY-MM-DD): 2022-07-27
//Date of Last Modification on Github: 2022-08-08
//C++ Version Used: ISO C++ 14
//Kinesis Version Tested: 1.14.40


#include <iostream>
#include <stdio.h>
#include <conio.h>

#include "Thorlabs.MotionControl.Benchtop.BrushlessMotor.h"

int main()
{
	// Uncomment this line (and TLI_UnitializeSimulations at the bottom of the page)
	// If you are using a simulated device
	//TLI_InitializeSimulations();

	// Change this line to reflect your device's serial number
	int serialNo = 103357054;

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

			printf("Channel 1 Homing\n");
			BMC_Home(testSerialNo, 1);
			// Wait for "Homing Complete" Message on channel 1
			BMC_WaitForMessage(testSerialNo, 1, &messageType, &messageId, &messageData);
			while (messageType != 2 || messageId != 0)
			{
				BMC_WaitForMessage(testSerialNo, 1, &messageType, &messageId, &messageData);
			}
			Sleep(500);
			printf("Channel 2 Homing\n");
			BMC_Home(testSerialNo, 2);
			BMC_WaitForMessage(testSerialNo, 2, &messageType, &messageId, &messageData);
			while (messageType != 2 || messageId != 0)
			{
				BMC_WaitForMessage(testSerialNo, 2, &messageType, &messageId, &messageData);
			}
			Sleep(500);
			printf("Both Channels Homed\n");

			// Set synchronous move parameters

			WORD arrID = 1; // Like the Highlander, there can only be 1
			WORD chanMask = 0x01 + 0x02; // mask for channels 1 and 2 (0x03 for channel 3)
			WORD numPoints = 300; // 100 Total x/y positions
			WORD startIndex = 0; // Only non-zero if using more than 256 positions
			WORD repeatCount = 0;
			WORD endCycleIndex = numPoints;
			WORD startCycleIndex = 1;
			DWORD deceleration = 100;

			const WORD arrSize = numPoints;
			long* timePos = new long[arrSize]; // Necessary to make array legal

			/*
			* Synch positions accepted as 1D array of time and position
			* These are in groups of 1 + numOfChannels, e.g. if using 2 channels, then
			* each position is defined by a 3 value group:
			* 0 100000 100000
			* 80 200000 200000 represents two moves
			*
			* Positions are given in device units
			* Times are given as time since last move in device time units
			* 1 device time unit = 0.1024 ms
			*/

			WORD hundredMS = 977; // Approx 100 ms in device

			// Get device params, including device units
			MOT_StageAxisParameters chan1Params;
			MOT_StageAxisParameters chan2Params;

			BMC_GetStageAxisParamsBlock(testSerialNo, 1, &chan1Params);
			BMC_GetStageAxisParamsBlock(testSerialNo, 2, &chan2Params);

			int chan1DevUnit = chan1Params.countsPerUnit; // gets the device unit count per mm or degree
			int chan2DevUnit = chan2Params.countsPerUnit;

			printf("chan 1 dev unit per mm: %d\n", chan1DevUnit);
			printf("chan 2 dev unit per mm: %d\n", chan2DevUnit);
			
			Sleep(500);
			int xHome = BMC_GetPosition(testSerialNo, 1);
			int yHome = BMC_GetPosition(testSerialNo, 2); // in dev units
			Sleep(500);

			printf("chan 1 position: %d\n", xHome);
			printf("chan 2 position: %d\n", yHome);

			int chan1inc = chan1DevUnit / 50; // incremental move
			int chan2inc = chan2DevUnit / 50;

			// The following is just one way of building a large array with less code.
			// It's not necessarily the best practice

			timePos[0] = 0; // starting at 0 seconds
			timePos[1] = xHome + chan1inc;
			timePos[2] = yHome + chan2inc;

			int j = 2; // starting with increment of 0.04mm
			for (int i = 3; i < 300; i += 3) {
				timePos[i] = hundredMS;
				timePos[i + 1] = xHome + (chan1inc * j);
				timePos[i + 2] = yHome + (chan2inc * j);
				j++;
			}

			printf("Time pos 0: %d, Time pos 1: %d, Time pos 2: %d\n", timePos[0], timePos[1], timePos[2]);
			printf("Time pos 30: %d, Time pos 31: %d, Time pos 32: %d\n", timePos[30], timePos[31], timePos[32]);
			printf("Time pos[-3]: %d, time pos[-2]: %d, Time pos [-1]: %d\n", timePos[arrSize - 3], timePos[arrSize - 2], timePos[arrSize - 1]);

			BMC_SetMultiChannelMoveArrayParams(testSerialNo,
				arrID,
				startCycleIndex,
				endCycleIndex,
				repeatCount,
				numPoints,
				deceleration);

			BMC_SetMultiChannelMoveArraySection(testSerialNo,
				arrID,
				chanMask,
				numPoints,
				startIndex,
				timePos);

			Sleep(750);
			// start synchronous movement
			printf("Starting Synchronous movement...\n");
			BMC_StartMultiChannelMoveArray(testSerialNo, arrID, chanMask);

			Sleep(numPoints * 100/2); // each move takes ~100 ms
			BMC_StopProfiledSynchronously(testSerialNo, chanMask);
		}

	}
	// We'll not be setting velocity parameters or moving

	// Uncomment this line if you are using simulations
	//TLI_UninitializeSimulations();
	printf("Program Finished. Press any key and Enter to exit.\n");
	char c = _getch();
}