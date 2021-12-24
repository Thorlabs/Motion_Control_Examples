// Example_KSG101.cpp : Defines the entry point for the console application.

// stdafx.h includes header files for several pre-compiled Windows binaries
#include "stdafx.h"

#include <stdlib.h>
#include <conio.h>

// include device specific header
#include "Thorlabs.MotionControl.KCube.StrainGauge.h"

int __cdecl wmain(int argc, wchar_t* argv[])
{
    if(argc < 1)
    {
        printf("Usage = Example_KSG101 [serial_no]\r\n");
        char c = _getch();
        return 1;
    }

    int serialNo = 59837825;
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
        TLI_GetDeviceListByTypeExt(serialNos, 100, 59);

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
        if(SG_Open(testSerialNo) == 0)
        {
            // start the device polling at 200ms intervals
            SG_StartPolling(testSerialNo, 200);

            // NOTE The following uses Sleep functions to simulate timing
            // In reality, the program should read the status to check that commands have been completed
            Sleep(1000);

            // Set reference
            SG_SetZero(testSerialNo);
            Sleep(1000);

            bool overrange;
            SG_SetDisplayMode(testSerialNo, TSG_Display_Modes::TSG_Position);
            int voltage = SG_GetReadingExt(testSerialNo, false, &overrange);
            printf("Device %s position = %d\r\n", testSerialNo, voltage);
            Sleep(1000);

            SG_SetDisplayMode(testSerialNo, TSG_Display_Modes::TSG_Voltage);
            int pos = SG_GetReadingExt(testSerialNo, false, &overrange);
            printf("Device %s voltage = %d\r\n", testSerialNo, pos);
            Sleep(1000);

            SG_SetDisplayMode(testSerialNo, TSG_Display_Modes::TSG_Force);
            int force = SG_GetReadingExt(testSerialNo, false, &overrange);
            printf("Device %s Force = %d\r\n", testSerialNo, force);
            Sleep(1000);

            // stop polling
            SG_StopPolling(testSerialNo);
            // close device
            SG_Close(testSerialNo);
        }
    }

    char c = _getch();
    return 0;
}
