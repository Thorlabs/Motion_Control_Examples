/*
KDC101 Simple Example
Date of Creation(YYYY-MM-DD): 2025-08-25
Date of Last Modification on Github: 2025-08-25
C++ Version Used: ISO C++ 14
XA Version Tested: 1.2.7
Tested with Z825B motor
Description: This example demonstrates how to connect to a KDC101 device, home it, and move it by 2 mm.
*/
#include <iostream>
#include <windows.h>
#include "tlmc_xa_native_api.h"

int main()
{
    TLMC_ResultCode startupResult = TLMC_Startup(nullptr);
    if (startupResult != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "SDK Startup failed.  " <<  std::endl;
        return 1;
    }

    TLMC_DeviceHandle hDevice;
    const char* serialNo = "27268054"; // Replace with your device's serial number
    TLMC_ResultCode resultCode = TLMC_Open(serialNo, nullptr, TLMC_OperatingModes::TLMC_OperatingMode_Default, &hDevice);

    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to open device."  << std::endl;
        std::cerr << "Possible causes: Device is turned off, not connected, or serial number is incorrect." << std::endl;
        TLMC_Shutdown();
        return 2;
    }

    std::cout << "Device opened successfully." << std::endl;

    // Home device
    resultCode = TLMC_Home(hDevice, TLMC_InfiniteWait);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Homing failed.  "  << std::endl;
        TLMC_Close(hDevice);
        TLMC_Shutdown();
        return 3;
    }
    std::cout << "Homing successful." << std::endl;

    // Move device 2 mm
    double distance = 2;
    int64_t valueInDeviceUnits;
    TLMC_ResultCode convertResult = TLMC_ConvertFromPhysicalToDevice(hDevice, TLMC_ScaleType::TLMC_ScaleType_Distance, TLMC_Unit_Type::TLMC_Unit_Millimetres, distance, &valueInDeviceUnits);
    if (convertResult != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Conversion failed. "  << std::endl;
        TLMC_Close(hDevice);
        TLMC_Shutdown();
        return 4;
    }

    resultCode = TLMC_Move(hDevice, TLMC_MoveMode::TLMC_MoveMode_Absolute, valueInDeviceUnits, 10000);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Move failed. "  << std::endl;
        TLMC_Close(hDevice);
        TLMC_Shutdown();
        return 5;
    }
    std::cout << "Moved 2 mm" << std::endl;

    if (TLMC_Close(hDevice) != TLMC_ResultCodes::TLMC_Success)
        std::cerr << "Device close failed." << std::endl;
    else
        std::cout << "Device closed." << std::endl;

    TLMC_Shutdown();
    return 0;
}
