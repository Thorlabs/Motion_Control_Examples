%% Header
% KDC101.m
% Created Date 20230906
% Last modified date 20230906
% Matlab Version R2022a
% Thorlabs DLL version Kinesis 1.14.35
%% Notes
%
% Example for the KDC101 using the MTS50 stage

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
SimulationManager.Instance.InitializeSimulations();

%% Connect
%Build Device List loads the connected devices to available memory
DeviceManagerCLI.BuildDeviceList();

% Update serial number to correct device
serialNumber = '27000001'; 
timeout_val=60000;

% Connect to the controller
device = KCubeDCServo.CreateKCubeDCServo(serialNumber);
device.Connect(serialNumber);

device.WaitForSettingsInitialized(5000);
device.StartPolling(250);

%Pull the enumeration values from the DeviceManagerCLI
optionTypeHandle = devCLI.AssemblyHandle.GetType('Thorlabs.MotionControl.DeviceManagerCLI.DeviceSettingsSectionBase+SettingsUseOptionType');
optionTypeEnums = optionTypeHandle.GetEnumValues(); 

%Load Settings to the controller
motorConfiguration = device.LoadMotorConfiguration(serialNumber);
motorConfiguration.LoadSettingsOption = optionTypeEnums.Get(1); % File Settings Option
motorConfiguration.DeviceSettingsName = 'MTS50'; %The actuator type needs to be set here. This specifically loads an MTS50
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

%% Disconnect from controller
device.StopPolling();
device.Disconnect();

%% Close Simulations (Comment out if using a real device)
SimulationManager.Instance.UninitializeSimulations();