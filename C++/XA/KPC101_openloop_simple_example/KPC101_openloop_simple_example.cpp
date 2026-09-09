/*
KPC101 Openloop Simple Example
Date of Creation: 05/14/2026
Last Modified Date on Github: 09/08/2026
C++ Version Used: ISO C++ 14
XA Version Tested: 1.9.3
Description: This example demonstrates how to connect to a KPC30X device,
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

    // Open device.
    TLMC_DeviceHandle hDevice;
    const char* deviceSerialNo = "1234"; // Replace with your device's serial number.
    TLMC_ResultCode resultCode = TLMC_Open(deviceSerialNo, nullptr, TLMC_OperatingModes::TLMC_OperatingMode_Default, &hDevice);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to open device." << std::endl;
        std::cerr << "Possible causes: Device is turned off, not connected, or device serial number is incorrect." << std::endl;
        TLMC_Shutdown();
        return 2;
    }
    std::cout << "Device opened successfully." << std::endl;

    // Enable device.
    resultCode = TLMC_SetEnableState(hDevice, TLMC_EnableState::TLMC_Enabled, 60000);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to enable device." << std::endl;
        TLMC_Close(hDevice);
        TLMC_Shutdown();
        return 3;
    }
    std::cout << "device enabled successfully." << std::endl;

    // Zero device.
    resultCode = TLMC_PZ_SetZero(hDevice, 60000);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to zero voltage." << std::endl;
        TLMC_Close(hDevice);
        TLMC_Shutdown();
        return 4;
    }
    std::cout << "Voltage zeroed successfully." << std::endl;

    // Set to open loop mode.
    resultCode = TLMC_PZ_SetPositionControlMode(hDevice, TLMC_PZ_PositionControlMode::TLMC_PZ_PositionControlMode_OpenLoop, 60000);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to set open loop mode." << std::endl;
        TLMC_Close(hDevice);
        TLMC_Shutdown();
        return 5;
    }
    std::cout << "Set open loop mode successfully." << std::endl;

    // Set output voltage.
    int16_t outputVoltage = 10;
    resultCode = TLMC_PZ_SetOutputVoltage(hDevice, outputVoltage);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to set output voltage." << std::endl;
        TLMC_Close(hDevice);
        TLMC_Shutdown();
        return 6;
    }
    std::cout << "Output voltage set successfully." << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(200));

    // Get output voltage.
    int16_t readbackVoltage;
    resultCode = TLMC_PZ_GetOutputVoltage(hDevice, &readbackVoltage, 60000);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to get output voltage." << std::endl;
        TLMC_Close(hDevice);
        TLMC_Shutdown();
        return 7;
    }
    std::cout << "New output voltage is: " << readbackVoltage << std::endl;
        
    // Close device, shutdown XA system.
    if (TLMC_Close(hDevice) != TLMC_ResultCodes::TLMC_Success)
        std::cerr << "Device close failed." << std::endl;
    else
        std::cout << "Device closed." << std::endl;
    TLMC_Shutdown();
    return 0;
}