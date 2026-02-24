%% Header
% K10CR1.m
% Created Date: 2024-08-22
% Last modified date: 2024-08-22
% Matlab Version: R2023b
% Thorlabs DLL version: Kinesis 1.14.49
%% Notes
%
% Example for the K10CR1 intergrated rotation stage
%%
%% Start of code
clear all; close all; clc


%Load Assemblies
devCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.DeviceManagerCLI.dll');
genCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.GenericMotorCLI.dll');
motCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.IntegratedStepperMotorsCLI.dll');

import Thorlabs.MotionControl.DeviceManagerCLI.*
import Thorlabs.MotionControl.GenericMotorCLI.*
import Thorlabs.MotionControl.IntegratedStepperMotorsCLI.*

%% Create Simulation (Comment out for real device)
%SimulationManager.Instance.InitializeSimulations(); 

%Initialize Device List
DeviceManagerCLI.BuildDeviceList();
DeviceManagerCLI.GetDeviceListSize();

%Update the serial number for the stage to the one being used.
serial_num='55000114';
timeout_val=60000;

%Set up device and configuration
device = CageRotator.CreateCageRotator(serial_num);
device.Connect(serial_num);
device.WaitForSettingsInitialized(5000);

motorSettings = device.LoadMotorConfiguration(serial_num);
currentDeviceSettings = device.MotorDeviceSettings;

motorSettings.UpdateCurrentConfiguration();
deviceUnitConverter = device.UnitConverter();

device.StartPolling(250);
device.EnableDevice();
pause(1); %wait to make sure device is enabled

%Home device
device.Home(timeout_val);
fprintf('Motor homed.\n');

%Can use specific roatation methods. Like MoveContinous() but need to pull enum values for direction parameter.
directionOptions = genCLI.AssemblyHandle.GetType("Thorlabs.MotionControl.GenericMotorCLI.AdvancedMotor.GenericAdvancedMotorCLI+MotorDirection");
Forward = directionOptions.GetEnumValues(0);
Backward = directionOptions.GetEnumValues(1);

device.MoveContinous(Forward);
pause(10)
device.Stop(timeout_val)

%Here, we move the stage to 10 units
device.MoveTo(10, timeout_val);

%Read out current position
pos = System.Decimal.ToDouble(device.Position);
fprintf('The motor position is %d.\n',pos);

%Stop connection to device
device.StopPolling()
device.Disconnect()

%% Close Simulations (Comment out if using a real device)
%SimulationManager.Instance.UninitializeSimulations(); %Close Simulations