%% Header
% LTS150.m
% Created Date: 2024-01-16
% Last modified date: 2024-01-16
% Matlab Version: R2023b
% Thorlabs DLL version: Kinesis 1.14.44
%% Notes
%
% Example for the LTS150 intergrated stage stage
%%
%% Start of code
clear all; close all; clc

%% Add and Import Assemblies
devCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.DeviceManagerCLI.dll');
genCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.GenericMotorCLI.dll');
motCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.IntegratedStepperMotorsCLI.dll');

import Thorlabs.MotionControl.DeviceManagerCLI.*
import Thorlabs.MotionControl.GenericMotorCLI.*
import Thorlabs.MotionControl.IntegratedSteppeMotorsCLI.*

%% Create Simulation (Comment out for real device)
%SimulationManager.Instance.InitializeSimulations(); 

%% Connect to device
% Build Device list
DeviceManagerCLI.BuildDeviceList();

% Update serial number to correct device
serialNumber = '45210154'; 
timeout_val = 60000;

% Connect to the Device 
device = Thorlabs.MotionControl.IntegratedStepperMotorsCLI.LongTravelStage.CreateLongTravelStage(serialNumber);
device.Connect(serialNumber) 

% Settings should be initialized as soon as the channel is connected. 
device.WaitForSettingsInitialized(50000);
device.StartPolling(250);

%Load Settings
motorConfiguration = device.LoadMotorConfiguration(serialNumber);

%Enable the device and start sending commands
device.EnableDevice();
pause(1); %wait to make sure Ch1 is enabled

% Homing
fprintf("Homing...\n")
device.Home(timeout_val);
fprintf("Homed\n")

% Moving
fprintf("Moving...\n")
device.MoveTo(50, timeout_val)
fprintf("Moved.\n")

%% Disconnect the device
device.StopPolling();
device.Disconnect(true);

%% Close Simulations (Comment out if using a real device)
%SimulationManager.Instance.UninitializeSimulations(); %Close Simulations

