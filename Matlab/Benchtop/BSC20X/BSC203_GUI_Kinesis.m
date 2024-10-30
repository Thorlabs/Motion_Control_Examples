%% Header
% BSC203_GUI_Kinesis.m
% Created Date: 2024-10-21
% Last modified date: 2024-10-21
% Matlab Version: R2023b
% Thorlabs DLL version: Kinesis 1.14.44
%% Notes
%
% Example for the BSC203 opening the Kinesis GUI
%%
%% Start of code

clear all; close all; clc

%% Load Assemblies
NET.addAssembly('System.Windows.Forms');
NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.DeviceManagerCLI.dll');
NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.DeviceManagerUI.dll');
NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.GenericMotorCLI.dll');
NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.Benchtop.StepperMotorCLI.dll');
NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.Benchtop.StepperMotorUI.dll');
NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.Controls.dll');

%% Import
import System.Windows.Forms.*;
import Thorlabs.MotionControl.DeviceManagerCLI.*
import Thorlabs.MotionControl.DeviceManagerUI.*
import Thorlabs.MotionControl.GenericMotorCLI.*
import Thorlabs.MotionControl.Benchtop.StepperMotorCLI.*
import Thorlabs.MotionControl.Benchtop.StepperMotorUI.*
import Thorlabs.MotionControl.Controls.*

%% Code
% Initialise Simulations - Uncomment if using the simulator
SimulationManager.Instance.InitializeSimulations();

% Enter devices serial number here, must be enclosed 
% by '' as it is treated as a string not an int
serialNo = '70000001';
% Create form
f = Form;

% Build Device List
DeviceManagerCLI.BuildDeviceList();

% This example only creates one control change the name of the
% Control and assemblies to the controller being used
device = BenchtopStepperControl();
device.LargeView = true;

% Fills the window with the control
device.Dock = DockStyle.Fill;
try
    % Try/Catch statement used to disconnect correctly after an error
    device.SerialNumber = serialNo;
    device.ChannelNumber = 1;
    device.CreateDevice();
    
    % Add the UI to the WinForm control
    f.Controls.Add(device);
    f.Show

    pause; % wait for user input to close device

catch e
    fprintf("Error has caused the program to stop, disconnecting..\n")
    fprintf(e.identifier);
    fprintf("\n");
    fprintf(e.message);
end

device.CloseDevice();
f.Close();

% Unitialise Simulations - Uncomment if using the simulator
SimulationManager.Instance.UninitializeSimulations();