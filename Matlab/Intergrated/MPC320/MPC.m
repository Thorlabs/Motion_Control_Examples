%% Header
% MPC320.m
% Created Date: 2024-08-22
% Last modified date: 2024-08-22
% Matlab Version: R2023b
% Thorlabs DLL version: Kinesis 1.14.49
%% Notes
%
% Example for the MPC320 intergrated rotation stage
%%
%% Start of code
clear all; close all; clc

%% Add and Import Assemblies
devCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.DeviceManagerCLI.dll');
polCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.PolarizerCLI.dll');


import Thorlabs.MotionControl.DeviceManagerCLI.*
import Thorlabs.MotionControl.PolarizerCLI.*


%% Create Simulation (Comment out for real device)
%SimulationManager.Instance.InitializeSimulations(); 

%% Connect to device
% Build Device list
DeviceManagerCLI.BuildDeviceList();

% Update serial number to correct device
serialNumber = '38000001'; 

% Connect to the Device 
device = Polarizer.CreatePolarizer(serialNumber); %The output of this line must be suppressed
device.Connect(serialNumber) 

device.StartPolling(250);

device.EnableDevice();


paddle1 = PolarizerPaddles.Paddle1;

paddle2 = PolarizerPaddles.Paddle2;

Paddle3 = PolarizerPaddles.Paddle3;
% Move the stage
device.Home(paddle, 6000);
pause(2);

device.Home(paddle, 6000);
pause(2);

device.Home(paddle, 6000);
pause(2);

device.MoveTo(new_pos, paddle1, 6000);
pause(2);

device.MoveTo(new_pos, paddle2, 6000);
pause(2);

device.MoveTo(new_pos, paddle3, 6000);
pause(2);

%% Disconnect the channel and chassis
device.StopPolling();
device.Disconnect(true);


%% Close Simulations (Comment out if using a real device)
SimulationManager.Instance.UninitializeSimulations(); %Close Simulations