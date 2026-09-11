/*
Title: UMCx
Created date: 24/06/2026
Last Modified Date: 24/06/2026
C++ version used: ISO C++ 14
Thorlabs DLL version: 1.6.8.27431
This example demonstrates how to set-up the communication for the Thorlabs
UMCx controllers with a brushless stage, home it, and move it by 5 mm or degrees.
*/

#include <iostream>
#include <string>
#include <windows.h>
#include <tlmc_xa_native_api.h>
#include <thread>
#include <chrono>

int main()
{
    // Start up XA
    TLMC_ResultCode startupResult = TLMC_Startup(nullptr);
    if (startupResult != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "SDK Startup failed." << std::endl;
        return 1;
    }

    TLMC_DeviceHandle hDevice;
    const char* deviceSerialNo = "121000020"; // Replace with your device's serial number
    TLMC_ResultCode resultCode = TLMC_Open(deviceSerialNo, nullptr, TLMC_OperatingModes::TLMC_OperatingMode_Default, &hDevice);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to open device." << std::endl;
        std::cerr << "Possible causes: Device is turned off, not connected, or channel serial number is incorrect." << std::endl;
        TLMC_Shutdown();
        return 2;
    }
    std::cout << "Device opened successfully." << std::endl;

    // Create channel handle and assign channel serial number
    TLMC_DeviceHandle hChannel;
    std::string channelSerialNoStr = std::string(deviceSerialNo) + std::to_string(-1);
    const char* channelSerialNo = channelSerialNoStr.c_str();

    // Open the channel
    resultCode = TLMC_Open(channelSerialNo, nullptr, TLMC_OperatingModes::TLMC_OperatingMode_Default, &hChannel);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to open device." << std::endl;
        std::cerr << "Possible causes: Device is turned off, not connected, or channel serial number is incorrect." << std::endl;
        TLMC_Shutdown();
        return 3;
    }
    std::cout << "Channel 1 opened successfully." << std::endl;

    // Enable channel 1
    resultCode = TLMC_SetEnableState(hChannel, TLMC_EnableState::TLMC_Enabled, 60000);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to enable channel 1." << std::endl;
        TLMC_Close(hChannel);
        TLMC_Shutdown();
        return 4;
    }
    std::cout << "Channel 1 enabled successfully." << std::endl;

    // Home channel 1
    resultCode = TLMC_Home(hChannel, TLMC_InfiniteWait);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Homing failed." << std::endl;
        TLMC_Close(hChannel);
        TLMC_Shutdown();
        return 5;
    }
    std::cout << "Homing successful." << std::endl;

    // Convert 5 mm to device units (physical -> device)
    double distanceMM = 5.0;
    int64_t valueInDeviceUnits;
    resultCode = TLMC_ConvertFromPhysicalToDevice(hChannel, TLMC_ScaleType::TLMC_ScaleType_Distance, TLMC_Unit_Type::TLMC_Unit_Millimetres, distanceMM, &valueInDeviceUnits);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Conversion failed." << std::endl;
        TLMC_Close(hChannel);
        TLMC_Shutdown();
        return 6;
    }
    std::cout << "Conversion from 5 mm successful. Value in device units: " << valueInDeviceUnits << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(500));


    // Absolute move to 5 mm
    resultCode = TLMC_Move(hChannel, TLMC_MoveMode::TLMC_MoveMode_Absolute, valueInDeviceUnits, 60000);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Move failed." << std::endl;
        TLMC_Close(hChannel);
        TLMC_Shutdown();
        return 7;
    }
    std::cout << "Absolute move successful." << std::endl;

    // Get the current position in device units
    int32_t currentPosition;
    resultCode = TLMC_GetPositionCounter(hChannel, &currentPosition, 60000);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to get current position." << std::endl;
        TLMC_Close(hChannel);
        TLMC_Shutdown();
        return 8;
    }

    // Convert the position to physical units and print both position values
    double valueInPhysicalUnits; 
    TLMC_Unit_Type physicalUnit;
    resultCode = TLMC_ConvertFromDeviceToPhysical(hChannel, TLMC_ScaleType::TLMC_ScaleType_Distance, currentPosition, &valueInPhysicalUnits, &physicalUnit);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Conversion failed." << std::endl;
        TLMC_Close(hChannel);
        TLMC_Shutdown();
        return 9;
    }

    std::cout << "New current position is:\nDevice Units: " << currentPosition << "\nPhysical Units: " << valueInPhysicalUnits << std::endl;

    // Close channel, disconnect and close device, shut down XA
    if (TLMC_Close(hChannel) != TLMC_ResultCodes::TLMC_Success)
        std::cerr << "Channel 1 close failed." << std::endl;
    else
        std::cout << "Channel 1 closed." << std::endl;

    if (TLMC_Close(hDevice) != TLMC_ResultCodes::TLMC_Success)
        std::cerr << "Device close failed." << std::endl;
    else
        std::cout << "Device closed." << std::endl;

    TLMC_Shutdown();
}