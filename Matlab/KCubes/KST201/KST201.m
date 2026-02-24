%% Header
% Title: KST201.m
% Created Date: 2025-01-31
% Last modified date: 2025-01-31
% Matlab Version: R2022b
% Thorlabs DLL version: Kinesis 1.14.50
%% Notes:
% Tested with KST201 using the ZFS13 actuator
% The example shows how to change homing velocity, homing direction, moving velocity and trigger settings. Then it homes and and moves 
clear; close all; clc

%% Add and Import Assemblies
devCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.DeviceManagerCLI.dll');
genCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.GenericMotorCLI.dll');
motCLI = NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.KCube.StepperMotorCLI.dll');

import Thorlabs.MotionControl.DeviceManagerCLI.*
import Thorlabs.MotionControl.GenericMotor.CLI.*
import Thorlabs.MotionControl.KCube.StepperMotorCLI.*

%% Create Simulation (Comment out for real device)
%SimulationManager.Instance.InitializeSimulations();

serialNumber = '26006239'; 
timeout_val=20000;

%methodsview('Thorlabs.MotionControl.GenericMotorCLI.GenericMotorCLI')

%% Connect
DeviceManagerCLI.BuildDeviceList();

% Connect to the controller
device = KCubeStepper.CreateKCubeStepper(serialNumber);
device.Connect(serialNumber);

% Get info and display description
device_info = device.GetDeviceInfo();
disp(device_info.Description)

device.WaitForSettingsInitialized(5000);
device.StartPolling(250);

pause(1);
device.EnableDevice();
pause(1);

% Configure device
device_config = device.LoadMotorConfiguration(device.DeviceID);

% Set homing velocity
device.SetHomingVelocity(0.5);
homingvelocity=device.GetHomingVelocity();
disp("Homing velocity set to:")
disp(System.Decimal.ToDouble(homingvelocity));

% Change homing direction (not necessary in most cases)
optionTypeHandle=genCLI.AssemblyHandle.GetType('Thorlabs.MotionControl.GenericMotorCLI.Settings.HomeSettings+HomeDirection');
optionTypeEnums=optionTypeHandle.GetEnumValues();
homingparams=device.GetHomingParams();
homingparams.Direction=optionTypeEnums.Get(1);
fprintf("New homing direction:");
disp(homingparams.Direction)

%Trigger Settings: set trigger to stop on trigger low
trigPortModeEnum = genCLI.AssemblyHandle.GetType('Thorlabs.MotionControl.GenericMotorCLI.Settings.KCubeTriggerConfigSettings+TriggerPortMode');
trigPortModeEnumVals = trigPortModeEnum.GetEnumValues(); 

trigPortPolarityEnum = genCLI.AssemblyHandle.GetType('Thorlabs.MotionControl.GenericMotorCLI.Settings.KCubeTriggerConfigSettings+TriggerPolarity');
trigPortPolarityEnumVals = trigPortPolarityEnum.GetEnumValues(); 

triggerConfigParams = device.GetTriggerConfigParams();
triggerConfigParams.Trigger1Mode = trigPortModeEnumVals.Get(5); % 5 corresponds to stop. 
triggerConfigParams.Trigger1Polarity = trigPortPolarityEnumVals.Get(1);% 1 corresponds to low
device.SetTriggerConfigParams(triggerConfigParams);

%Get current velocity parameters
vel_params = device.GetVelocityParams();
fprintf('Velocity: \t%1.2f, \t Acceleration: \t%1.2f\n\n',...
    System.Decimal.ToDouble(vel_params.MaxVelocity),System.Decimal.ToDouble(vel_params.Acceleration));

%Set new velocity and acceleration
device.SetVelocityParams(0.5,0.5);     
vel_params = device.GetVelocityParams();
fprintf('New velocity: \t%1.2f, \tNew acceleration: \t%1.2f\n\n',...
    System.Decimal.ToDouble(vel_params.MaxVelocity),System.Decimal.ToDouble(vel_params.Acceleration));

pause(1);

% Home the stage
fprintf("homing...");
device.Home(timeout_val);
fprintf("homed\n");


% Move the stage
fprintf("Moving...\n")
device.MoveTo(1.0,timeout_val);
fprintf("Moved\n")

%Disconnect from controller
device.StopPolling();
device.Disconnect();

%% Close Simulations (Comment out if using a real device)
%SimulationManager.Instance.UninitializeSimulations();
