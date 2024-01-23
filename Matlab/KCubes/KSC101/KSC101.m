%% Header
% Title: KSC101.m
% Created Date: 2024-01-16
% Last modified date: 2024-01-16
% Matlab Version: R2023b
% Thorlabs DLL version: Kinesis 1.14.44
%% Notes:
%
% Example for the KSC101

%% Start of code
clear all; close all; clc

%% Add and Import Assemblies
devCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.DeviceManagerCLI.dll');
genCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.GenericMotorCLI.dll');
solCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.KCube.SolenoidCLI.dll');

import Thorlabs.MotionControl.DeviceManagerCLI.*
import Thorlabs.MotionControl.KCube.SolenoidCLI.*
import Thorlabs.MotionControl.GenericMotorCLI.*

%% Create Simulation (Comment out for real device)
SimulationManager.Instance.InitializeSimulations();

%% Connect
% Builds Device list
DeviceManagerCLI.BuildDeviceList();
% Prints the number of connected devices
DeviceManagerCLI.GetDeviceListSize();

%Update serial number to correct device
serial_num='68000001';
timeout_val=60000;

%Connect to controller
device = KCubeSolenoid.CreateKCubeSolenoid(serial_num);
device.Connect(serial_num);
device.WaitForSettingsInitialized(5000);

device.StartPolling(250);
device.EnableDevice();
pause(1) %wait to make sure device is enabled

%%
%Pull the enumeration values from the SolenoidCLI
modesHandle = solCLI.AssemblyHandle.GetType("Thorlabs.MotionControl.KCube.SolenoidCLI.SolenoidStatus+OperatingModes");
statesHandle = solCLI.AssemblyHandle.GetType("Thorlabs.MotionControl.KCube.SolenoidCLI.SolenoidStatus+OperatingStates");
modesEnums = modesHandle.GetEnumValues();
statesEnums = statesHandle.GetEnumValues();

device.SetOperatingMode(modesEnums.GetValue(0)); % Manual mode, change the interger value for other modes
pause(5);
fprintf("Opening the Shutter\n")
device.SetOperatingState(statesEnums.GetValue(0)); % Opens the shutter
pause(5);
fprintf("Closing the Shutter\n")
device.SetOperatingState(statesEnums.GetValue(1)); % Closes the shutter
pause(5);

%% Disconnect from controller
device.StopPolling();
device.Disconnect();

%% Close Simulations (Comment out if using a real device)
SimulationManager.Instance.UninitializeSimulations();
