/*
KIM101 Simple Example
Date of Creation(YYYY-MM-DD): 2022-01-14
Date of Last Modification on Github: 2022-09-21
C++ Version Used: ISO C++ 14
Kinesis Version Tested: 1.14.40
*/

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

// include device-specific header file
#include "Thorlabs.MotionControl.KCube.InertialMotor.h"

int __cdecl wmain(int argc, wchar_t* argv[])
{

	// Uncomment this line (and TLI_UnitializeSimulations at the bottom of the file)
	// if you are using simulated devices.
	//TLI_InitializeSimulations();

	// Change the serial number to match the one found on your device
    int serialNo = 85000001;

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

        // Search serial numbers for given serial number
        if (strstr(serialNos, testSerialNo)) {
            printf("Device %s found", testSerialNo);
        }
        else {
            printf("Device %s Not Found", testSerialNo);
            return -1;
        }

        // open device
        if(KIM_Open(testSerialNo) == 0)
        {
            // start the device polling at 200ms intervals
            KIM_StartPolling(testSerialNo, 200);

            // initalize current position to zero
            KIM_SetPosition(testSerialNo, KIM_Channels::Channel1, 0);

			// It is often good practice to allow some time for the device to accept commands
            Sleep(200);

            // Move to Absolute position (in device units)
            KIM_MoveAbsolute(testSerialNo, KIM_Channels::Channel1, 1000);
            Sleep(200);
            printf("Device %s moving to 1000\r\n", testSerialNo);
            Sleep(5000);
                    
            int pos = KIM_GetCurrentPosition(testSerialNo, KIM_Channels::Channel1);
            printf("Device %s position is %d\r\n", testSerialNo, pos);

            // Move Jog using jog settings
            KIM_MoveJog(testSerialNo, KIM_Channels::Channel1, KIM_TravelDirection::Forward);
            Sleep(200);
            printf("Device %s jogging\r\n", testSerialNo);
            Sleep(2000);
                    
            pos = KIM_GetCurrentPosition(testSerialNo, KIM_Channels::Channel1);
            printf("Device %s position is %d\r\n", testSerialNo, pos);


            // stop polling
            KIM_StopPolling(testSerialNo);
            // close device
            KIM_Close(testSerialNo);
        }
    }

	// Uncomment this line if you are using simulations
	//TLI_UnitializeSimulations;
    char c = _getch();
    return 0;
}
