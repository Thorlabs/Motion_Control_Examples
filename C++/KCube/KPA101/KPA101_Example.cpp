// Example_KPA101.cpp : Defines the entry point for the console application.

// stdafx.h imports header files for several pre-compiled Windows binaries
#include "stdafx.h"

#include <stdlib.h>
#include <conio.h>

// include device specific
#include "Thorlabs.MotionControl.KCube.PositionAligner.h"

int __cdecl wmain(int argc, wchar_t* argv[])
{
    if(argc < 1)
    {
        printf("Usage = Example_KPA101 [serial_no] [xPos: optional (+/-32767), yPos: optional (+/-32767)]\r\n");
        char c = _getch();
        return 1;
    }

    int serialNo = 89837825;
    if(argc > 1)
    {
        serialNo = _wtoi(argv[1]);
    }

    // identify and access device
    char testSerialNo[16];
    sprintf_s(testSerialNo, "%d", serialNo);

    QD_Position demandPosition = {0,0};
    if(argc > 3)
    {
        demandPosition.x = _wtoi(argv[2]);
        demandPosition.y = _wtoi(argv[3]);
    }

    // Build list of connected device
    if (TLI_BuildDeviceList() == 0)
    {
        // get device list size 
        short n = TLI_GetDeviceListSize();
        // get BBD serial numbers
        char serialNos[100];
        TLI_GetDeviceListByTypeExt(serialNos, 100, 69);

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

    char c = _getch();
    return 0;
}
