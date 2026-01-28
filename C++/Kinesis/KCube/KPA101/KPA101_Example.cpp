/*
KPA101 Simple Example
Date of Creation(YYYY-MM-DD): 2021-12-24
Date of Last Modification on Github: 2022-09-21
C++ Version Used: ISO C++ 14
Kinesis Version Tested: 1.14.40
*/

#include <iostream>
#include <stdlib.h>
#include <conio.h>

// include device specific
#include "Thorlabs.MotionControl.KCube.PositionAligner.h"

int __cdecl wmain()
{

    // Uncomment this line if using Simulations
    //TLI_InitializeSimulations();
    int serialNo = 89837825;

    // identify and access device
    char testSerialNo[16];
    sprintf_s(testSerialNo, "%d", serialNo);

    QD_Position demandPosition = {0,0};

    // demandPosition.x = 1;
    //demandPosition.y = 1;


    // Build list of connected device
    if (TLI_BuildDeviceList() == 0)
    {
        // get device list size 
        short n = TLI_GetDeviceListSize();
        // get BBD serial numbers
        char serialNos[100];
        TLI_GetDeviceListByTypeExt(serialNos, 100, 69);

        // Search serial numbers for given serial number
        if (strstr(serialNos, testSerialNo)) {
            printf("Device %s found", testSerialNo);
        }
        else {
            printf("Device %s Not Found", testSerialNo);
            return -1;
        }

        // open device
        if(QD_Open(testSerialNo) == 0)
        {
            // start the device polling at 200ms intervals
            QD_StartPolling(testSerialNo, 200);

            // NOTE The following uses Sleep functions to simulate timing
            // In reality, the program should read the status to check that commands have been completed
            Sleep(1000);

            printf("Device %s set open loop mode\r\n", testSerialNo);
            QD_SetOperatingMode(testSerialNo, QD_OperatingMode::QD_OpenLoop, false);
            Sleep(100);

            QD_SetPosition(testSerialNo, &demandPosition);
            printf("Device %s set demand position (%d, %d)\r\n", testSerialNo, demandPosition.x, demandPosition.y);
            Sleep(1000);

            QD_Readings readPosition = {0,0};
            QD_GetReading(testSerialNo, &readPosition);
            printf("Device %s readings:\r\n", testSerialNo);
            printf("\tdemanded position (%d, %d)\r\n", readPosition.demandedPos.x, readPosition.demandedPos.y);
            printf("\tposition difference (%d, %d)\r\n", readPosition.posDifference.x, readPosition.posDifference.y);
            printf("\tsum %d\r\n", readPosition.sum);

            Sleep(100);

            // stop polling
            QD_StopPolling(testSerialNo);
            // close device
            QD_Close(testSerialNo);
        }
    }

    // Uncomment this line if using simulations
    //TLI_UninitializeSimulations();
    char c = _getch();
    return 0;
}
