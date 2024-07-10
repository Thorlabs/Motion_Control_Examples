%% Header
% Title: KIM101.m
% Created Date: 2024-01-16
% Last modified date: 2024-07-02
% Matlab Version: R2023b
% Thorlabs DLL version: Kinesis 1.14.44
%% Notes:
%
% Example for the KIM101

%% Start of code
clear all; close all; clc

%% Add and Import Assemblies
devCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.DeviceManagerCLI.dll');
genCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.GenericMotorCLI.dll');
motCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.KCube.InertialMotorCLI.dll');

import Thorlabs.MotionControl.DeviceManagerCLI.*
import Thorlabs.MotionControl.GenericMotorCLI.*
import Thorlabs.MotionControl.KCube.InertialMotorCLI.*

%% Create Simulation (Comment out for real device)
%SimulationManager.Instance.InitializeSimulations();

%% Connect
% Builds Device list
DeviceManagerCLI.BuildDeviceList();

% Will need to update serial number to correct device
serial_num='97100058';
timeout_val=60000;

%Connect to controller
device = KCubeInertialMotor.CreateKCubeInertialMotor(serial_num);
device.Connect(serial_num);

try
    % Try/Catch statement used to disconnect correctly after an error

    device.WaitForSettingsInitialized(5000);
    
    device.StartPolling(250);
    device.EnableDevice();
    pause(1) %wait to make sure device is enabled
    
    % Pull the Enums needed
    channelsHandle = motCLI.AssemblyHandle.GetType('Thorlabs.MotionControl.KCube.InertialMotorCLI.InertialMotorStatus+MotorChannels');
    
    channelsEnums = channelsHandle.GetEnumValues();
    jogDirectionHandle = motCLI.AssemblyHandle.GetType('Thorlabs.MotionControl.KCube.InertialMotorCLI.InertialMotorJogDirection');
    jogDirectionEnums = jogDirectionHandle.GetEnumValues();
    
    % Zero the actuator
    fprintf("Zero the actuator\n")
    device.SetPositionAs(channelsEnums.GetValue(0), 0);
    
    % Jog the Actuator
    fprintf("Jog the actuator forwards\n")
    device.Jog(channelsEnums.GetValue(0), jogDirectionEnums.GetValue(0), timeout_val);
catch e
    fprintf("Error has caused the program to stop, disconnecting..\n")
    fprintf(e.identifier);
    fprintf("\n");
    fprintf(e.message);
end

%Disconnect from controller
device.StopPolling();
device.Disconnect();

%% Close Simulations (Comment out for real device)
%SimulationManager.Instance.UninitializeSimulations();