%% Header
% Title: PDXC2.m
% Created Date: 2024-07-02
% Last modified date: 2024-07-02
% Matlab Version: R2023b
% Thorlabs DLL version: Kinesis 1.14.44
%% Notes:
%
% Example for the PDXC2

%% Start of code
clear all; close all; clc

%% Add and Import Assemblies
devCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.DeviceManagerCLI.dll');
genCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.GenericPiezoCLI.dll');
motCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.Benchtop.PiezoCLI.dll');

import Thorlabs.MotionControl.DeviceManagerCLI.*
import Thorlabs.MotionControl.GenericPiezoCLI.*
import Thorlabs.MotionControl.Benchtop.PiezoCLI.*
import Thorlabs.MotionControl.Benchtop.PiezoCLI.PDXC2.*


%% Create Simulation (Comment out for real device)
SimulationManager.Instance.InitializeSimulations();

%% Connect
%Build Device List loads the connected devices to available memory
DeviceManagerCLI.BuildDeviceList();

% Update serial number to correct device
serialNumber = '112123456'; 
timeout_val=60000;

% Connect to the controller
device = InertiaStageController.CreateInertiaStageController(serialNumber);
device.Connect(serialNumber);

try
    % Try/Catch statement used to disconnect correctly after an error

    device.WaitForSettingsInitialized(5000);
    device.StartPolling(250);
    
    %Pull the enumeration values from the DeviceManagerCLI
    optionTypeHandle = devCLI.AssemblyHandle.GetType('Thorlabs.MotionControl.DeviceManagerCLI.DeviceConfiguration+DeviceSettingsUseOptionType');
    optionTypeEnums = optionTypeHandle.GetEnumValues(); 

    
    %Load Settings to the controller
    piezoConfiguration = device.GetPDXC2Configuration(serialNumber,optionTypeEnums.Get(0));
    deviceSettings = PDXC2Settings.GetSettings(piezoConfiguration);
    device.SetSettings(deviceSettings,true,true);
    
    % Enable the device and start sending commands
    device.EnableDevice();
    pause(1); %wait to make sure the cube is enabled

    controlModeHandle = genCLI.AssemblyHandle.GetType('Thorlabs.MotionControl.GenericPiezoCLI.Piezo.PiezoControlModeTypes');
    controlModeEnums = controlModeHandle.GetEnumValues();
    device.SetPositionControlMode(controlModeEnums.Get(1))

    % Home the stage
    fprintf("Homing...\n")
    device.Home(timeout_val);
    fprintf("Homed\n\n")

catch e
    fprintf("Error has caused the program to stop, disconnecting..\n");
    fprintf(e.identifier);
    fprintf("\n");
    fprintf(e.message);
end

%% Disconnect from controller
device.StopPolling();
device.Disconnect();

%% Close Simulations (Comment out if using a real device)
SimulationManager.Instance.UninitializeSimulations();