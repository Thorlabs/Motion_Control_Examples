// Example_KLD101.cpp : Defines the entry point for the console application.

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

// Include device-specific header file
#include "Thorlabs.MotionControl.KCube.LaserDiode.h"


int __cdecl wmain(int argc, wchar_t* argv[])
{

	// Uncomment this line (and TLI_UnitializeSimulations at the bottom of the page)
	// If you are using a simulated device

	// Change this line to reflect your device's serial number
	int serialNo = 98000001;


    // Optionally Adjust the setpoint of your device
    WORD setPoint = 100;

    // identify and access device
    char testSerialNo[16];
    sprintf_s(testSerialNo, "%d", serialNo);

    // Build list of connected devices
    if (TLI_BuildDeviceList() == 0)
    {
        // get device list size 
        short n = TLI_GetDeviceListSize();
        // get KLD serial numbers
        char serialNos[100];
        TLI_GetDeviceListByTypeExt(serialNos, 100, 98);

        // Search serial numbers for given serial number
        if (strstr(serialNos, testSerialNo)) {
            printf("Device %s found", testSerialNo);
        }
        else {
            printf("Device %s Not Found", testSerialNo);
            return -1;
        }

        // open device
        if(LD_Open(testSerialNo) == 0)
        {
            // start the device polling at 200ms intervals
            LD_StartPolling(testSerialNo, 200);

            // NOTE The following uses Sleep functions to simulate timing
            // In reality, the program should read the status to check that commands have been completed
            Sleep(1000);

            LD_SetOpenLoopMode(testSerialNo);
            LD_EnableOutput(testSerialNo);
            LD_SetLaserSetPoint(testSerialNo, setPoint);
            printf("Device %s set point %d\r\n", testSerialNo, setPoint);
            Sleep(1000);

            WORD readCurrent = LD_GetLaserDiodeCurrentReading(testSerialNo);
            float waFactor = LD_GetWACalibFactor(testSerialNo);
            printf("Device %s read current %d\r\n", testSerialNo, readCurrent);
            printf("Device %s read power %f\r\n", testSerialNo, (float)readCurrent * waFactor);

            Sleep(1000);

            // stop polling
            LD_StopPolling(testSerialNo);
            // close device
            LD_Close(testSerialNo);
        }
    }

	// Uncomment this line if you are using simulations
	//TLI_UnitializeSimulations;
    char c = _getch();
    return 0;
}
