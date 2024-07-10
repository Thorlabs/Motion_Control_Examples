%% Header
% BSC101.m
% Created Date: 2024-01-16
% Last modified date: 2024-07-02
% Matlab Version: R2023b
% Thorlabs DLL version: Kinesis 1.14.44
%% Notes
%
% Example for the BSC201 using the HDR50 stage
%%
%% Start of code
clear all; close all; clc

%% Add and Import Assemblies
devCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.DeviceManagerCLI.dll');
genCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.GenericMotorCLI.dll');
motCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.Benchtop.StepperMotorCLI.dll');

import Thorlabs.MotionControl.DeviceManagerCLI.*
import Thorlabs.MotionControl.GenericMotorCLI.*
import Thorlabs.MotionControl.Benchtop.StepperMotorCLI.*

%% Create Simulation (Comment out for real device)
%SimulationManager.Instance.InitializeSimulations(); 

%% Connect to device
% Build Device list
DeviceManagerCLI.BuildDeviceList();

% Update serial number to correct device
serialNumber = '40878473'; 
timeout_val = 60000;

% Connect to the Device 
device = BenchtopStepperMotor.CreateBenchtopStepperMotor(serialNumber); %The output of this line must be suppressed
device.Connect(serialNumber) 
try
    % Try/Catch statement used to disconnect correctly after an error

    % Channels are connected using the same serial number
    % Connect to the channel
    channel = device.GetChannel(1);
    % Settings should be initialized as soon as the channel is connected. 
    channel.WaitForSettingsInitialized(50000);
    channel.StartPolling(250);
    
    %Pull the enumeration values from the DeviceManagerCLI
    optionTypeHandle = devCLI.AssemblyHandle.GetType('Thorlabs.MotionControl.DeviceManagerCLI.DeviceSettingsSectionBase+SettingsUseOptionType');
    optionTypeEnums = optionTypeHandle.GetEnumValues(); 
    
    %Load Settings to the controller
    motorConfiguration = channel.LoadMotorConfiguration(serialNumber);
    motorConfiguration.LoadSettingsOption = optionTypeEnums.Get(1); % File Settings Option
    motorConfiguration.DeviceSettingsName = 'HDR50'; %The actuator type needs to be set here. This specifically loads a HDR50
    factory = ThorlabsBenchtopStepperMotorSettingsFactory();
    channel.SetSettings(factory.GetSettings(motorConfiguration), true, false);
    
    %Enable the device and start sending commands
    channel.EnableDevice();
    pause(1); %wait to make sure Ch1 is enabled
    
    % Home the stage
    fprintf("Homing...\n")
    channel.Home(timeout_val);
    fprintf("Homed\n")
    
    % Move the stage
    fprintf("Moving...\n")
    channel.MoveTo(50, timeout_val)
    fprintf("Moved.\n")
catch
    fprintf("Error has caused the program to stop, disconnecting..\n")
    fprintf(e.identifier);
    fprintf("\n");
    fprintf(e.message);
end

%% Disconnect the channel and chassis
channel.StopPolling();
channel.Disconnect(true);
device.Disconnect(true);

%% Close Simulations (Comment out if using a real device)
SimulationManager.Instance.UninitializeSimulations(); %Close Simulations

