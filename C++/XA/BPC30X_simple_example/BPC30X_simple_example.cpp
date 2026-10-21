/*
BPC30x Simple Example
Date of Creation: 03/10/2026
Last Modified Date on Github: 09/08/2026
C++ Version Used: ISO C++ 14
XA Version Tested: 1.9.3
Description: This example demonstrates how to connect to a BPC30X device and channel,
             zero it, set max voltage values, and output a voltage.
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

    // Open channel-1 (BPC30X controller).
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

    // Zero channel.
    resultCode = TLMC_PZ_SetZero(hChannel, 60000);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to zero voltage." << std::endl;
        TLMC_Close(hChannel);
        TLMC_Shutdown();
        return 4;
    }
    std::cout << "Voltage zeroed successfully." << std::endl;

    // Set maximum output voltage.
    int16_t maxOutputVoltage = 25;
    resultCode = TLMC_PZ_SetMaxOutputVoltage(hChannel, maxOutputVoltage);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to set maximum output voltage." << std::endl;
        TLMC_Close(hChannel);
        TLMC_Shutdown();
        return 5;
    }
    std::cout << "Maximum output set successfully." << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(200));

    // Get maximum output voltage.
    struct TLMC_PZ_MaxOutputVoltageParams voltageParams;
    resultCode = TLMC_PZ_GetMaxOutputVoltageParams(hChannel, &voltageParams, 60000);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to get maximum output voltage." << std::endl;
        TLMC_Close(hChannel);
        TLMC_Shutdown();
        return 6;
    }
    std::cout << "New maximum output voltage is: " << voltageParams.maxOutputVoltage << std::endl;

    // Set output voltage.
    int16_t outputVoltage = 10;
    resultCode = TLMC_PZ_SetOutputVoltage(hChannel, outputVoltage);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to set output voltage." << std::endl;
        TLMC_Close(hChannel);
        TLMC_Shutdown();
        return 7;
    }
    std::cout << "Output voltage set successfully." << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(200));

    // Get output voltage.
    int16_t readbackVoltage;
    resultCode = TLMC_PZ_GetOutputVoltage(hChannel, &readbackVoltage, 60000);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to get output voltage." << std::endl;
        TLMC_Close(hChannel);
        TLMC_Shutdown();
        return 8;
    }
    std::cout << "New output voltage is: " << readbackVoltage << std::endl;
        
    // Close channel, disconnect and close device, shutdown XA system.
    if (TLMC_Close(hChannel) != TLMC_ResultCodes::TLMC_Success)
        std::cerr << "Channel close failed." << std::endl;
    else
        std::cout << "Channel closed." << std::endl;
    TLMC_Shutdown();
    return 0;
}