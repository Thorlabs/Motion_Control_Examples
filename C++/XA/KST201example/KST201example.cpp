/*
KST201 Example
Date of Creation(YYYY-MM-DD): 2025-11-07
Date of Last Modification on Github: 2025-11-07
C++ Version Used: ISO C++ 14
XA Version Tested: 1.2.7
Tested with ZFS25B motor
Description: This example demonstrates how to connect to a KDC101 device, home it, and move it by 3 mm.
*/
#include <iostream>
#include <stdio.h>
#include "tlmc_xa_native_api.h"

int main() {
    TLMC_Unit unit = TLMC_Unit::TLMC_Unit_Millimetres;

    if (TLMC_Startup(nullptr) == TLMC_ResultCodes::TLMC_Success)
    {
        TLMC_DeviceHandle hDevice = TLMC_InvalidDevice;

        if (TLMC_Open("26006127", nullptr, TLMC_OperatingModes::TLMC_OperatingMode_Default, &hDevice) == TLMC_ResultCodes::TLMC_Success)
        {
            TLMC_Home(hDevice, TLMC_InfiniteWait);

            int32_t counter = 0;
            TLMC_GetPositionCounter(hDevice, &counter, TLMC_InfiniteWait);
            printf("Position counter before move: %d\n", counter);

            int64_t relativeDistanceInPhysicalUnits = 3; // 2 mm
            printf("Requested distance in physical units: %d mm\n", (int)relativeDistanceInPhysicalUnits);

            int64_t relativeDistanceInDeviceUnits;
            if (TLMC_ConvertFromPhysicalToDevice(hDevice, TLMC_ScaleType::TLMC_ScaleType_Distance, TLMC_Unit::TLMC_Unit_Millimetres, 3, &relativeDistanceInDeviceUnits) == TLMC_ResultCode::TLMC_Success) {
                printf("Distance in device units: %d\n", (int)relativeDistanceInDeviceUnits);
            }

			// Perform relative move with converted distance
            if (TLMC_Move(hDevice, TLMC_MoveMode::TLMC_MoveMode_Relative, relativeDistanceInDeviceUnits, 10000) == TLMC_ResultCode::TLMC_Success)
            {
				printf("Move completed\n");
            }
            else {
                printf("Error moving\n");
            }

			TLMC_GetPositionCounter(hDevice, &counter, TLMC_InfiniteWait);
            printf("Position counter after move: %d\n", counter);

            
            if (TLMC_Close(hDevice) != TLMC_ResultCodes::TLMC_Success)
                std::cerr << "Device close failed." << std::endl;
            else
                std::cout << "Device closed." << std::endl;

        }
        else {
            std::cout << "Failed to open device" << std::endl;
        }

        TLMC_Shutdown();
        return 0;
    }
}