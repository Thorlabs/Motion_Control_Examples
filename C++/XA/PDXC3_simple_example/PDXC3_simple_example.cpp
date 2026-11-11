/*
PDXC3 Simple Example
Date of Creation: 10/19/2026
Last Modified Date on Github: 10/19/2026
C++ Version Used: ISO C++ 14
XA Version Tested: 1.11.0
Description: This example demonstrates how to connect to a PDXC3 device and channel,
             set to Open Loop mode, and perform a jog move.
*/
#include <iostream>
#include <string>
#include <windows.h>
#include "tlmc_xa_native_api.h"

int main()
{
    // Startup XA system.
    TLMC_ResultCode startupResult = TLMC_Startup(nullptr);
    if (startupResult != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "SDK Startup failed." << std::endl;
        return 1;
    }

    TLMC_ResultCode resultCode;

    // Create simulation device for testing purposes. 
    // Uncomment this part(and TLMC_RemoveSimulation() at the end on main)
    // If you are using a simulated device
    //std::string pdxc3SimulationDefinition = "{\
    //            \"PartNumber\": \"PDXC3\",\
    //            \"SerialNumber\" : \"129000000\",\
    //            \"Channels\" :\[\
    //                {\
    //                    \"BayNumber\": \"1\",\
    //                    \"SerialNumber\" : \"129000001\",\
    //                    \"ActuatorType\" : \"PDX1\"\},\
    //                {\
    //                    \"BayNumber\": \"2\",\
    //                    \"SerialNumber\" : \"129000002\",\
    //                    \"ActuatorType\" : \"PDX1\"\},\
    //                {\
    //                    \"BayNumber\": \"3\",\
    //                    \"SerialNumber\" : \"129000003\",\
    //                    \"ActuatorType\" : \"PDX1\"\}\
    //            ]\}";

    //resultCode = TLMC_CreateSimulation(pdxc3SimulationDefinition.c_str());
    //if (resultCode != TLMC_ResultCodes::TLMC_Success)
    //{
    //    std::cerr << "Failed to create the simulation device." << std::endl;
    //    TLMC_Shutdown();
    //    return 2;
    //}
    

    // Open PDXC3
    TLMC_DeviceHandle hdevice;
    const char* deviceSerialNo = "129000000"; // Replace with your device's serial number.
    resultCode = TLMC_Open(deviceSerialNo, nullptr, TLMC_OperatingModes::TLMC_OperatingMode_Default, &hdevice);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to open device." << std::endl;
        std::cerr << "Possible causes: Device is turned off, not connected, or serial number is incorrect." << std::endl;
        TLMC_Shutdown();
        return 3;
    }
    std::cout << "Device opened successfully." << std::endl;

	// Get the handle for Channel 1
	TLMC_DeviceHandle hChannel;
    resultCode = TLMC_GetChannel(hdevice, 1, &hChannel);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to get channel." << std::endl;
        TLMC_Disconnect(hdevice);
        TLMC_Close(hdevice);
        TLMC_Shutdown();
        return 4;
	}

    // Enable Channel 1.
    resultCode = TLMC_SetEnableState(hChannel, TLMC_EnableState::TLMC_Enabled, 60000);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to enable channel." << std::endl;
        TLMC_Disconnect(hdevice);
        TLMC_Close(hdevice);
        TLMC_Shutdown();
        return 5;
    }
    std::cout << "Channel enabled successfully." << std::endl;
	Sleep(500); 

	//Set Position Control Mode to Open Loop Mode
	resultCode = TLMC_PZ_SetPositionControlMode(hChannel, TLMC_PZ_PositionControlMode::TLMC_PZ_PositionControlMode_OpenLoop, 60000);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to set position control mode." << std::endl;
        TLMC_Disconnect(hdevice);
        TLMC_Close(hdevice);
        TLMC_Shutdown();
        return 6;
	}

    // Set Open Loop jog step size to 100 steps.
    TLMC_PZIM_JogParams jogParams;
    TLMC_PZIM_GetJogParams(hChannel, &jogParams, 60000);
    jogParams.openLoopStepSize = 100; // Set step size to 100
    resultCode = TLMC_PZIM_SetJogParams(hChannel, &jogParams);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to set jog parameters." << std::endl;
        TLMC_Disconnect(hdevice);
        TLMC_Close(hdevice);
        TLMC_Shutdown();
        return 7;
	}

	// Execute a jog move in the forward direction.
    resultCode = TLMC_Move(hChannel, TLMC_MoveMode::TLMC_MoveMode_JogForward, 0, 60000);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Move failed." << std::endl;
        TLMC_Disconnect(hdevice);
        TLMC_Close(hdevice);
        TLMC_Shutdown();
        return 8;
    }
    std::cout << "Jog move successful." << std::endl;

    // Get and print current position.
    int32_t currentPosition;
	resultCode = TLMC_PZIM_GetCurrentPosition(hChannel, &currentPosition, 60000);
    if (resultCode != TLMC_ResultCodes::TLMC_Success)
    {
        std::cerr << "Failed to get current position." << std::endl;
        TLMC_Disconnect(hdevice);
        TLMC_Close(hdevice);
        TLMC_Shutdown();
        return 9;
    }
    std::cout << "New current position is: " << currentPosition << std::endl;

	// Disconnect device
    if (TLMC_Disconnect(hdevice) != TLMC_ResultCodes::TLMC_Success)
        std::cerr << "Device disconnect failed." << std::endl;
    else
		std::cout << "Device disconnected." << std::endl;

	// Close device
    if (TLMC_Close(hdevice) != TLMC_ResultCodes::TLMC_Success)
        std::cerr << "Device close failed." << std::endl;
    else
		std::cout << "Device closed." << std::endl;

    //Uncomment this line if you are using Simulations
    //TLMC_RemoveSimulation(pdxc3SimulationDefinition.c_str());

	// Shutdown XA system
    TLMC_Shutdown();
    return 0;
}