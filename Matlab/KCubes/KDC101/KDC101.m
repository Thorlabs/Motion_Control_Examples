%% Header
% Title: KDC101.m
% Created Date: 2024-01-16
% Last modified date: 2024-07-02
% Matlab Version: R2023b
% Thorlabs DLL version: Kinesis 1.14.44
%% Notes:
%
% Example for the KDC101 using the PRM1/M-Z8 stage

%% Start of code
clear all; close all; clc

%% Add and Import Assemblies
devCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.DeviceManagerCLI.dll');
genCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.GenericMotorCLI.dll');
motCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.KCube.DCServoCLI.dll');

import Thorlabs.MotionControl.DeviceManagerCLI.*
import Thorlabs.MotionControl.GenericMotorCLI.*
import Thorlabs.MotionControl.KCube.DCServoCLI.*

%% Create Simulation (Comment out for real device)
%SimulationManager.Instance.InitializeSimulations();

%% Connect
%Build Device List loads the connected devices to available memory
DeviceManagerCLI.BuildDeviceList();

% Update serial number to correct device
serialNumber = '27500876'; 
timeout_val=60000;

% Connect to the controller
device = KCubeDCServo.CreateKCubeDCServo(serialNumber);
device.Connect(serialNumber);

try
    % Try/Catch statement used to disconnect correctly after an error

    device.WaitForSettingsInitialized(5000);
    device.StartPolling(250);
    
    %Pull the enumeration values from the DeviceManagerCLI
    optionTypeHandle = devCLI.AssemblyHandle.GetType('Thorlabs.MotionControl.DeviceManagerCLI.DeviceSettingsSectionBase+SettingsUseOptionType');
    optionTypeEnums = optionTypeHandle.GetEnumValues(); 
    
    %Load Settings to the controller
    motorConfiguration = device.LoadMotorConfiguration(serialNumber);
    motorConfiguration.LoadSettingsOption = optionTypeEnums.Get(1); % File Settings Option
    motorConfiguration.DeviceSettingsName = 'PRM1-Z8'; %The actuator type needs to be set here. This specifically loads an PRM1-Z8
    factory = KCubeMotor.KCubeDCMotorSettingsFactory();
    device.SetSettings(factory.GetSettings(motorConfiguration), true, false);
    
    % Enable the device and start sending commands
    device.EnableDevice();
    pause(1); %wait to make sure the cube is enabled
    
    % Home the stage
    fprintf("Homing...\n")
    device.Home(timeout_val);
    fprintf("Homed\n\n")
    
    % Move the stage
    fprintf("Moving...\n")
    device.MoveTo(10.0,timeout_val);
    fprintf("Moved\n")
catch e
    fprintf("Error has caused the program to stop, disconnecting..\n")
    fprintf(e.identifier);
    fprintf("\n");
    fprintf(e.message);
end

%% Disconnect from controller
device.StopPolling();
device.Disconnect();

%% Close Simulations (Comment out if using a real device)
SimulationManager.Instance.UninitializeSimulations();