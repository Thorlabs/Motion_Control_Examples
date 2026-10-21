/*
BSC20x Simple Example
Date of Creation: 05/05/2026
Last Modified Date on Github: 09/08/2026
C++ Version Used: ISO C++ 14
XA Version Tested: 1.9.3
Description: This example demonstrates how to connect to a BSC20x device and channel,
             home it, and perform an absolute move.
*/
#include <iostream>
#include <string>
#include <windows.h>
#include "tlmc_xa_native_api.h"
#include <thread>
#include <chrono>

int main()
{
    // Startup XA system.
    TLMC_ResultCode startupResult = TLMC_Startup(nullptr);
    if (startupResult != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "SDK Startup failed." << std::endl;
        return 1;
    }

    // Open channel-1 (BSC20x controller).
    TLMC_DeviceHandle hChannel;
    const char* deviceSerialNo = "1234"; // Replace with your device's serial number.
    std::string channelSerialNoStr = std::string(deviceSerialNo) + std::to_string(-1); 
    // Construct channel 1 serial number using Kinesis notation .
    const char* channelSerialNo = channelSerialNoStr.c_str();
    TLMC_ResultCode resultCode = TLMC_Open(channelSerialNo, nullptr, TLMC_OperatingModes::TLMC_OperatingMode_Default, &hChannel);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to open device." << std::endl;
        std::cerr << "Possible causes: Device is turned off, not connected, or channel serial number is incorrect." << std::endl;
        TLMC_Shutdown();
        return 2;
    }
    std::cout << "Device opened successfully." << std::endl;

    // Enable channel.
    resultCode = TLMC_SetEnableState(hChannel, TLMC_EnableState::TLMC_Enabled, 60000);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to enable channel." << std::endl;
        TLMC_Close(hChannel);
        TLMC_Shutdown();
        return 3;
    }
    std::cout << "Channel enabled successfully." << std::endl;

    // Home channel.
    resultCode = TLMC_Home(hChannel, 60000);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Homing failed." << std::endl;
        TLMC_Close(hChannel);
        TLMC_Shutdown();
        return 4;
    }
    std::cout << "Homing successful." << std::endl;

    // Convert 5 mm to device units (physical -> device).
    double distanceMM = 5.0;
    int64_t valueInDeviceUnits;
    resultCode = TLMC_ConvertFromPhysicalToDevice(hChannel, TLMC_ScaleType::TLMC_ScaleType_Distance, TLMC_Unit_Type::TLMC_Unit_Millimetres, distanceMM, &valueInDeviceUnits);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Conversion failed." << std::endl;
        TLMC_Close(hChannel);
        TLMC_Shutdown();
        return 5;
    }
    std::cout << "Conversion from 5 mm successful. Value in device units: " << valueInDeviceUnits << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(200));

    // Absolute move to 5 mm.
    resultCode = TLMC_Move(hChannel, TLMC_MoveMode::TLMC_MoveMode_Absolute, valueInDeviceUnits, 60000);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Move failed." << std::endl;
        TLMC_Close(hChannel);
        TLMC_Shutdown();
        return 6;
    }
    std::cout << "Absolute move successful." << std::endl;

    // Get and print current position.
    int32_t currentPosition;
    resultCode = TLMC_GetPositionCounter(hChannel, &currentPosition, 60000);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to get current position." << std::endl;
        TLMC_Close(hChannel);
        TLMC_Shutdown();
        return 7;
    }
    std::cout << "New current position is: " << currentPosition << std::endl;
        
    // Close channel, disconnect and close device, shutdown XA system.
    if (TLMC_Close(hChannel) != TLMC_ResultCodes::TLMC_Success)
        std::cerr << "Channel close failed." << std::endl;
    else
        std::cout << "Channel closed." << std::endl;
    TLMC_Shutdown();
    return 0;
}