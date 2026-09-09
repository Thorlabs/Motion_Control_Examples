% Title: KPC101 Openloop
% Modification Date: 09/09/2026
% Example Description:
% This example demonstrates how to connect to a KPC101 piezo controller,
% zero it, set open-loop position control mode, output a voltage, and read it back.

% Load the XA dll
NET.addAssembly('C:\Program Files\Thorlabs XA\SDK\.NET Framework (C#)\Libraries\x64\tlmc_xa_dotnet.dll');

import Thorlabs.MotionControl.XA.*
import Thorlabs.MotionControl.XA.Products.*
import Thorlabs.MotionControl.XA.Piezo.*

% Change this line to match the serial number on your device.
deviceId = '1234';

% Start up XA.
systemManager = SystemManager.Create();
systemManager.Startup();

% Open the KPC101 device.
[ret, device] = systemManager.TryOpenDevice(deviceId, '', OperatingModes.Default);
if ~ret
    fprintf('Failed to open device %s\n', deviceId);
    fprintf('Possible causes: device is turned off, not connected, or serial number is incorrect.\n');
    systemManager.Shutdown();
    return;
end
fprintf('Device %s opened successfully\n', deviceId);

try
    % Enable the device.
    device.SetEnableState(EnableState.Enabled, System.TimeSpan.FromSeconds(60));
    fprintf('Device enabled successfully.\n');

    % Zero the piezo.
    device.SetZero(System.TimeSpan.FromSeconds(60));
    fprintf('Voltage zeroed successfully.\n');

    % Set open-loop position control mode.
    device.SetPositionControlMode(PositionControlMode.OpenLoop, System.TimeSpan.FromSeconds(60));
    fprintf('Set open loop mode successfully.\n');

    % Set the output voltage.
    outputVoltage = int16(10);
    device.SetOutputVoltage(outputVoltage);
    fprintf('Output voltage set successfully.\n');
    System.Threading.Thread.Sleep(200);

    % Get the output voltage.
    readbackVoltage = device.GetOutputVoltage(System.TimeSpan.FromSeconds(60));
    fprintf('New output voltage is: %d\n', readbackVoltage);

catch ex
    fprintf('Exception: %s\n', ex.message);
end

% Close the device.
if ~isempty(device)
    device.Disconnect();
    device.Close();
end
fprintf('Device closed.\n');
% Shutdown XA.
systemManager.Shutdown();
