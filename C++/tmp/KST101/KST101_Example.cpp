// Example_KST101.cpp : Defines the entry point for the console application.

// stdafx.h imports several header files for pre-compiled Windows binaries
#include "stdafx.h"

#include <stdlib.h>
#include <conio.h>

// include device-specific header file
#include "Thorlabs.MotionControl.KCube.StepperMotor.h"


int __cdecl wmain(int argc, wchar_t* argv[])
{
    if(argc < 1)
    {
        printf("Usage = Example_KST101 [serial_no] [position: optional (0 - 1715200)] [velocity: optional (0 - 3838091)]\r\n");
        char c = _getch();
        return 1;
    }

    int serialNo = 80837825;
    if(argc > 1)
    {
        serialNo = _wtoi(argv[1]);
    }

    // get parameters from command line
    int position = 0;
    if(argc > 2)
    {
        position = _wtoi(argv[2]);
    }

    int velocity = 0;
    if(argc > 3)
    {
        velocity = _wtoi(argv[3]);
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
        TLI_GetDeviceListByTypeExt(serialNos, 100, 80);

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
        if(SCC_Open(testSerialNo) == 0)
        {
            // start the device polling at 200ms intervals
            SCC_StartPolling(testSerialNo, 200);

            Sleep(3000);
            // Home device
            SCC_ClearMessageQueue(testSerialNo);
            SCC_Home(testSerialNo);
            printf("Device %s homing\r\n", testSerialNo);

            // wait for completion
            WORD messageType;
            WORD messageId;
            DWORD messageData;
            SCC_WaitForMessage(testSerialNo, &messageType, &messageId, &messageData);
            while(messageType != 2 || messageId != 0)
            {
                SCC_WaitForMessage(testSerialNo, &messageType, &messageId, &messageData);
            }

            // set velocity if desired
            if(velocity > 0)
            {
                int currentVelocity, currentAcceleration;
                SCC_GetVelParams(testSerialNo, &currentAcceleration, &currentVelocity);
                SCC_SetVelParams(testSerialNo, currentAcceleration, velocity);
            }

            // move to position (channel 1)
            SCC_ClearMessageQueue(testSerialNo);
            SCC_MoveToPosition(testSerialNo, position);
            printf("Device %s moving\r\n", testSerialNo);

            // wait for completion
            SCC_WaitForMessage(testSerialNo, &messageType, &messageId, &messageData);
            while(messageType != 2 || messageId != 1)
            {
                SCC_WaitForMessage(testSerialNo, &messageType, &messageId, &messageData);
            }

            // get actual poaition
            int pos = SCC_GetPosition(testSerialNo);
            printf("Device %s moved to %d\r\n", testSerialNo, pos);

            // stop polling
            SCC_StopPolling(testSerialNo);
            // close device
            SCC_Close(testSerialNo);
        }
    }

    char c = _getch();
    return 0;
}
