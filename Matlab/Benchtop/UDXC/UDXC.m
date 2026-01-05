%% Header
% Title: UDXC.m
% Created Date: 2026-01-02
% Last modified date: 2026-01-02
% Matlab Version: R2023b
% Thorlabs DLL version: Kinesis 1.14.56
%% Notes:
%
% Example for the UDXC

%% Start of code
clear all; close all; clc

%% Add and Import Assemblies
devCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.DeviceManagerCLI.dll');
genCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.GenericPiezoCLI.dll');
motCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.Benchtop.PiezoCLI.dll');

import Thorlabs.MotionControl.DeviceManagerCLI.*
import Thorlabs.MotionControl.GenericPiezoCLI.Piezo.*
import Thorlabs.MotionControl.Benchtop.PiezoCLI.*
import Thorlabs.MotionControl.Benchtop.PiezoCLI.UDXC.*


%% Create Simulation (Comment out for real device)
%SimulationManager.Instance.InitializeSimulations();

%% Connect
%Build Device List loads the connected devices to available memory
DeviceManagerCLI.BuildDeviceList();

% Update serial number to correct device
serialNumber = '122514658'; 
timeout_val=60000;

% Connect to the controller
device = InertialStageController.CreateInertialStageController(serialNumber);
device.Connect(serialNumber);

try
    % Try/Catch statement used to disconnect correctly after an error

    device.WaitForSettingsInitialized(10000);
    device.StartPolling(250);
    device.EnableDevice();
    
    %Load Settings to the controller
    piezoConfiguration = device.GetUDXCConfiguration(serialNumber,optionTypeEnums.Get(0));
    deviceSettings = UDXCSettings.GetSettings(piezoConfiguration);
    device.SetSettings(deviceSettings,true,true);
    
    % Enable the device and start sending commands
    device.EnableDevice();
    pause(1); %wait to make sure the controller is enabled

    % Home the stage
    fprintf("Homing...\n")
    device.Home(timeout_val);
    fprintf("Homed\n\n")
    newPos=device.GetCurrentPosition();

    closeLoopPosition=100000;
    if(closeLoopPosition~=0)
        device.SetClosedLoopTarget(closeLoopPosition);

        % Get and Set the velocity and acceleration
        closedLoopParams = device.GetClosedLoopParameters();
        closedLoopParams.RefSpeed = 10000000; % velocity is set in nm/s
        closedLoopParams.Acceleration = 10000000; % acceleration is set in nm/s^2
        device.SetClosedLoopParameters(closedLoopParams);
        
        device.MoveStart();
        fprintf("Moving to %d nm\n",closeLoopPosition);

        %check position
        posCheckCnt=0;
        for i=0:200
            newPos=device.GetCurrentPosition();
            if abs(closeLoopPosition-newPos)<6000
                if(posCheckCnt>3)
                    break
                else 
                    pause(0.25);
                    posCheckCnt = posCheckCnt + 1;
                end
            else
                pause(0.25);
            end
        end
        fprintf("Moved to %d nm\n",newPos);
        

    end

catch e
    fprintf("Error has caused the program to stop, disconnecting..\n");
    fprintf(e.identifier);
    fprintf("\n");
    fprintf(e.message);
end

%% Disconnect from controller
device.StopPolling();
device.Disconnect(true);

%% Close Simulations (Comment out if using a real device)
%SimulationManager.Instance.UninitializeSimulations();