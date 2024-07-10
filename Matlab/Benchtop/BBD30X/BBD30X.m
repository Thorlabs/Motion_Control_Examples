%% Header
% BBD30X.m
% Created Date: 2024-01-23
% Last modified date: 2024-07-02
% Matlab Version: R2023b
% Thorlabs DLL version: Kinesis 1.14.44
%% Notes
%
% Example for the BBD303 using the DDR100 stage
%%
%% Start of code
clear all; close all; clc

%% Add and Import Assemblies
devCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.DeviceManagerCLI.dll');
genCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.GenericMotorCLI.dll');
motCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.Benchtop.BrushlessMotorCLI.dll');

import Thorlabs.MotionControl.DeviceManagerCLI.*
import Thorlabs.MotionControl.GenericMotorCLI.*
import Thorlabs.MotionControl.Benchtop.BrushlessMotorCLI.*

%% Create Simulation (Comment out for real device)
SimulationManager.Instance.InitializeSimulations(); 

%% Connect to device
% Build Device list
DeviceManagerCLI.BuildDeviceList();
DeviceManagerCLI.GetDeviceListSize();
DeviceManagerCLI.GetDeviceList();

% Input Parameters
serialNumber = '103000001'; % BBD30X controller serial number
timeout= 60000;
position = 10; % mm

% Connect to device
device = BenchtopBrushlessMotor.CreateBenchtopBrushlessMotor(serialNumber); %;The output of this line must be suppressed
device.Connect(serialNumber)
try
    % Try/Catch statement used to disconnect correctly after an error

    % Channels are connected using the same serial number
    % Connect to the channel
    channel = device.GetChannel(1); % Get Channel 1
    channel.WaitForSettingsInitialized(10000);
    channel.StartPolling(250);
    
    % Enable device on channel 1
    channel.EnableDevice();
    pause(3);
    
    motorSettings = channel.LoadMotorConfiguration(channel.DeviceID);
    pause(1);
    % Home Motor
    fprintf("Homing...\n")
    channel.Home(timeout);
    fprintf("Homed\n")
    pause(2);
    
    %% Move to position
    fprintf("Moving...\n")
    channel.MoveTo(position, timeout);
    fprintf("Moved\n")
    pause(1);
catch
    fprintf("Error has caused the program to stop, disconnecting..\n")
    fprintf(e.identifier);
    fprintf("\n");
    fprintf(e.message);
end

%% Disconnect
channel.StopPolling();
channel.DisableDevice();
device.Disconnect();

%% Close Simulations (Comment out if using a real device)
SimulationManager.Instance.UninitializeSimulations(); %Close Simulations

