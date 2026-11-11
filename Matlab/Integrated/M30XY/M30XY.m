%% Header
% M30XY.m
% Created Date: 2024-01-26
% Last modified date: 2024-07-02
% Matlab Version: R2022a
% Thorlabs DLL version: Kinesis 1.14.45
%% Notes
%
% Example for the M30XY

%Example for programming the Thorlabs M30XY
%% Load assemblies
NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.DeviceManagerCLI.dll');
NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.GenericMotorCLI.dll');
NET.addAssembly('C:\Program Files\Thorlabs\Kinesis\Thorlabs.MotionControl.Benchtop.DCServoCLI.dll');

%% Initialize Device List
import Thorlabs.MotionControl.DeviceManagerCLI.*
import Thorlabs.MotionControl.GenericMotorCLI.*
import Thorlabs.MotionControl.Benchtop.DCServoCLI.*

%methodsview('Thorlabs.MotionControl.DeviceManagerCLI.DeviceManagerCLI')

%% Uncomment the following line for simulation
%SimulationManager.Instance.InitializeSimulations();


%% Initialize Device List
DeviceManagerCLI.BuildDeviceList();

%Should change the serial number below to the one being used.
serialNo='101000001';
timeoutVal=60000;

%Set up device and configuration
device =BenchtopDCServo.CreateBenchtopDCServo(serialNo);
device.Connect(serialNo);

try
    % Try/Catch statement used to disconnect correctly after an error

    channel = device.GetChannel(1);
    
    channel.WaitForSettingsInitialized(5000);
    
    %The polling loop requests regular status requests to the motor to ensure the program keeps track of the device. 
    channel.StartPolling(250);
    %Needs a delay so that the current enabled state can be obtained
    pause(1);
    %Enable the channel otherwise any move is ignored 
    channel.EnableDevice();
    %Needs a delay to give time for the device to be enabled
    pause(1);
    
    %Call LoadMotorConfiguration on the device to initialize the DeviceUnitConverter object required for real world unit parameters
    % - loads configuration information into channel
    motorConfiguration = channel.LoadMotorConfiguration(channel.DeviceID);
    
    % Display info about device
    deviceInfo = channel.GetDeviceInfo();
    disp( deviceInfo.Name);
    
    %Home
    channel.Home(timeoutVal);
    fprintf('Motor homed.\n');
    
    %Move to unit 10
    channel.MoveTo(10, timeoutVal);
    
    %Check Position
    pos = System.Decimal.ToDouble(channel.Position);
    fprintf('The motor position is %d.\n',pos);

catch e
    fprintf("Error has caused the program to stop, disconnecting..\n")
    fprintf(e.identifier);
    fprintf("\n");
    fprintf(e.message);
end

%% Close and Disconnect
channel.StopPolling()
device.Disconnect()

%% Close Simulations
%SimulationManager.Instance.UninitializeSimulations();